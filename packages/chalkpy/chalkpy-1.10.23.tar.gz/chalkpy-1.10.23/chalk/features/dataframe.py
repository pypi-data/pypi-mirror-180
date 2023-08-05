from __future__ import annotations

import collections.abc
import datetime
import enum
import functools
import operator
import pathlib
import warnings
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
    overload,
)

import polars as pl

try:
    import zoneinfo
except ImportError:
    # Zoneinfo was introduced in python 3.9
    from backports import zoneinfo

from dateutil import parser

from chalk.features.feature_field import Feature
from chalk.features.feature_wrapper import FeatureWrapper, unwrap_feature
from chalk.features.filter import Filter, TimeDelta
from chalk.serialization.codec import FEATURE_CODEC
from chalk.utils.collections import ensure_tuple, get_unique_item

if TYPE_CHECKING:
    import pandas as pd
    import pyarrow

    from chalk.features.feature_set import Features

else:
    try:
        import pandas as pd
    except ImportError:
        pd = None
    try:
        import pyarrow
    except ImportError:
        pyarrow = None

TDataFrame = TypeVar("TDataFrame", bound="DataFrame")


def _iso_parse(x: str, expected_tz: datetime.tzinfo | None) -> datetime.datetime:
    """This function converts the input into an expected timezone, and drops it, so we can cast it in polars with with_time_zone"""
    parsed = parser.isoparse(x)
    if parsed.tzinfo is not None and expected_tz is not None:
        # Convert the timezone
        parsed = parsed.astimezone(expected_tz)
    # Now drop the timezone
    return parsed.replace(tzinfo=None)


class DataFrameMeta(type):
    def __getitem__(cls, item: Any) -> Type[DataFrame]:
        from chalk.features.feature_set import Features

        # leaving untyped as we type the individual features as their object type
        # but item should really be Filter (expressions), Feature classes, or Feature instances
        cls = cast(Type[DataFrame], cls)

        item = ensure_tuple(item)

        # Disallow string annotations like DataFrame["User"].
        # Instead, the entire thing should be in quotes -- like "DataFrame[User]"
        for x in item:
            if isinstance(x, str):
                raise TypeError(
                    (
                        f'Annotation {cls.__name__}["{x}", ...] is unsupported. Instead, use a string for the entire annotation -- for example: '
                        f'"{cls.__name__}[{x}, ...]"'
                    )
                )

        # If doing multiple subscript, then keep the filters, but do not keep the individual columns
        # TODO: Validate that any new columns are a subset of the existing columns
        item = [*item, *cls.filters]

        new_filters: List[Filter] = []
        new_references_feature_set: Optional[Type[Features]] = None
        new_columns: List[Feature] = []

        for a in item:
            if isinstance(a, Filter):
                new_filters.append(a)
            elif isinstance(a, type) and issubclass(a, Features):
                if new_references_feature_set is not None:
                    raise ValueError(
                        f"Multiple referenced feature sets -- {new_references_feature_set} and {a} -- are not supported."
                    )
                new_references_feature_set = a
            elif isinstance(a, Feature):
                new_columns.append(a)
            elif isinstance(a, FeatureWrapper):
                new_columns.append(a._chalk_feature)
            elif isinstance(a, bool):
                # If we encounter a bool, that means we are evaluating the type annotation before
                # the ResolverAstParser had a chance to extract the source and rewrite the and/or/in operations
                # into expressions that return filters instead of booleans
                # This function will be called again for this annotation, so we can ignore it for now.
                pass
            else:
                raise TypeError(f"Invalid type for DataFrame[{a}]: {type(a)}")

        if len(new_columns) == 0 and new_references_feature_set is None:
            # This is possible if you have something like
            # Users.transactions[after('60d')]
            # In this case, keep all existing columns
            # But if you did
            # Users.transactions[Transaction.id, after('60d')]
            # Then keep only the id column
            new_columns = list(cls.__columns__)
            new_references_feature_set = cls.__references_feature_set__

        class SubclassedDataFrame(cls):
            filters = tuple(new_filters)
            __columns__ = tuple(new_columns)
            __references_feature_set__ = new_references_feature_set

            def __new__(cls: Type[TDataFrame], *args: Any, **kwargs: Any) -> TDataFrame:
                raise RuntimeError(
                    "A SubclassedDataFrame should never be instantiated. Instead, instantiate a DataFrame(...)."
                )

        return SubclassedDataFrame

    def __repr__(cls):
        cls = cast(Type[DataFrame], cls)
        elements = [str(x) for x in (*cls.filters, *cls.columns)]
        return f"DataFrame[{', '.join(elements)}]"

    @property
    def columns(cls) -> Tuple[Feature, ...]:
        # Computing the columns lazily as we need to implicitly parse the type annotation
        # to determine if a field is a has-many, and we don't want to do that on the
        # __getitem__ which could happen before forward references can be resolved
        # So, using a property on the metaclass, which acts like an attribute on the class, to
        # provide the dataframe columns
        from chalk.features.feature_field import Feature

        cls = cast(Type[DataFrame], cls)
        columns: Set[Feature] = set()
        for x in cls.__columns__:
            assert isinstance(x, Feature)
            # If a feature is directly specified, allow has-ones. But still do not allow has-many features
            assert not x.is_has_many, "Has-many features are not allowed to be specified within a DataFrame"
            columns.add(x)
        if cls.__references_feature_set__ is not None:
            # Only include the first-level feature types
            # Do not recurse has-ones and has-many as that could create an infinite loop
            for x in cls.__references_feature_set__.features:
                assert isinstance(x, Feature)
                if not x.is_has_many and not x.is_has_one:
                    columns.add(x)
        return tuple(columns)

    @property
    def references_feature_set(cls):
        from chalk.features.feature_set import FeatureSetBase

        cls = cast(Type[DataFrame], cls)
        if cls.__references_feature_set__ is not None:
            return cls.__references_feature_set__
        else:
            # Determine the unique @features cls that encompasses all columns
            root_ns = get_unique_item((x.root_namespace for x in cls.__columns__), "root ns")
        return FeatureSetBase.registry[root_ns]

    @property
    def namespace(cls) -> str:
        cls = cast(Type[DataFrame], cls)
        namespaces = [x.path[0].parent.namespace if len(x.path) > 0 else x.namespace for x in cls.columns]
        # Remove the pseudo-columns
        namespaces = [x for x in namespaces if not x.startswith("__chalk__")]
        return get_unique_item(namespaces, f"dataframe {cls.__name__} column namespaces")


class DataFrame(metaclass=DataFrameMeta):
    filters: ClassVar[Tuple[Filter, ...]] = ()
    columns: Tuple[Feature, ...]  # set via a @property on the metaclass
    __columns__: ClassVar[Tuple[Feature, ...]] = ()
    references_feature_set: Optional[Type[Features]]  # set via a @property on the metaclass
    __references_feature_set__: ClassVar[Optional[Type[Features]]] = None

    def __init__(
        self,
        data: Union[
            Dict[Union[str, Feature, FeatureWrapper, Any], Sequence[Features]],
            Sequence[Any],
            pl.DataFrame,
            pl.LazyFrame,
            pd.DataFrame,
            Any,  # Polars supports a bunch of other formats for initialization of a DataFrame
        ] = None,
        pandas_dataframe: Optional[pd.DataFrame] = None,  # For backwards compatibility
        convert_dtypes: bool = True,  # By default, data should match the dtype of the feature. However, when doing comparisions, data will be converted to bools, in which case it should no longer be validated.
    ):
        """Construct a Chalk DataFrame

        Args:
            data: The data. Can be an existing Pandas DataFrame, Polars DataFrame or LazyFrame, a sequence of feature instances,
                or a dict mapping a feature to a sequence of values.
            convert_dtypes: Whether to convert the data to match the dtype of the underlying feature.

        """
        from chalk.features.feature_set import Features, FeatureSetBase

        # Typing the keys of ``data`` as Any, as {FeatureCls.item: x} would be typed as the underlying annotation of the features cls
        if pandas_dataframe is not None:
            warnings.warn(
                DeprecationWarning("ChalkDataFrameImpl(pandas_dataframe=...) has been renamed to DataFrame(data=...)")
            )
            data = pandas_dataframe
        if pd is not None and isinstance(data, pd.DataFrame):
            # Convert the columns to root fqn strings
            # str(Feature) and str(FeatureWrapper) return the root fqns
            data = data.rename(columns={k: str(k) for k in data.columns})
            assert isinstance(data, pd.DataFrame)
            data.columns = data.columns.astype("string")
            data = pl.from_pandas(data)
        if not isinstance(data, (pl.LazyFrame, pl.DataFrame)):
            if isinstance(data, (collections.abc.Sequence)) and not isinstance(data, str):
                # If it is a sequence, it could be a sequence of feature classes instances
                # If so, set the columns by inspecting the feature classes
                # If columns are none, then inspect the data to determine if they are feature classes
                # Otherwise, if the columns are specified, do not introspect the list construction
                features_typ = None
                new_data: dict[str, list[Any]] = {}
                for row in data:
                    if not isinstance(row, Features):
                        raise ValueError("If specifying data as a sequence, it must be a sequence of Features")
                    if features_typ is None:
                        features_typ = type(row)
                        for x in row.features:
                            assert isinstance(x, Feature)
                            assert x.attribute_name is not None
                            try:
                                feature_val = getattr(row, x.attribute_name)
                            except AttributeError:
                                continue
                            new_data[x.root_fqn] = []

                    if features_typ != type(row):
                        raise ValueError("Cannot mix different feature classes in a DataFrame")
                    for x in row.features:
                        assert isinstance(x, Feature)
                        assert x.attribute_name is not None
                        try:
                            feature_val = getattr(row, x.attribute_name)
                        except AttributeError:
                            if x.root_fqn in new_data:
                                raise ValueError(f"Feature {x.root_fqn} is not defined in all feature sets.")
                            continue
                        if x.is_has_many:
                            raise ValueError("DataFrames within DataFrames are not supported")
                        if x.root_fqn not in new_data:
                            raise ValueError(f"Feature {x.root_fqn} is not defined in all feature sets.")
                        new_data[x.root_fqn].append(feature_val)
                data = new_data
            if isinstance(data, dict):
                # Convert the columns to root fqn strings
                # str(Feature) and str(FeatureWrapper) return the root fqns
                new_data_dict: Dict[str, Sequence[Any] | pl.Series] = {}
                for (k, v) in data.items():
                    v = [_preprocess_element(x) for x in v]

                    if convert_dtypes:
                        polars_dtype = FEATURE_CODEC.get_polars_dtype(str(k))
                        elements_as_series = _generate_empty_series_for_dtype(str(k), polars_dtype, 0)
                        null_element = _generate_empty_series_for_dtype(str(k), polars_dtype, 1)
                        for i, element in enumerate(v):
                            if element is None or isinstance(element, (list, tuple)) and len(element) == 0:
                                elements_as_series.append(null_element)
                            else:
                                element_as_series = pl.Series(name=str(k), values=[element])
                                if element_as_series.dtype != polars_dtype:

                                    if _polars_dtype_contains_struct(polars_dtype):
                                        # Cannot cast to a struct type. Instead, will error, so the user can ensure the underlying
                                        # dictionaries / dataclasses are of the correct type
                                        raise TypeError(
                                            (
                                                f"Expected field `{str(k)}` to have dtype `{str(polars_dtype)}`; got dtype `{str(element_as_series.dtype)}`"
                                                f" for element {element} at index {i}"
                                            )
                                        )
                                    else:
                                        try:
                                            if (
                                                isinstance(element_as_series.dtype, type)
                                                and issubclass(element_as_series.dtype, pl.Utf8)
                                                and isinstance(polars_dtype, pl.Datetime)
                                            ):
                                                if polars_dtype.tz is None:
                                                    element_as_series = element_as_series.apply(
                                                        lambda x: None if x is None else _iso_parse(x, None),
                                                    ).dt.with_time_zone(None)
                                                else:
                                                    tzinfo = zoneinfo.ZoneInfo(polars_dtype.tz)
                                                    element_as_series = element_as_series.apply(
                                                        lambda x: None if x is None else _iso_parse(x, tzinfo),
                                                    ).dt.with_time_zone(polars_dtype.tz)
                                            else:
                                                element_as_series = element_as_series.cast(polars_dtype)
                                        except (pl.ComputeError, pl.InvalidOperationError) as e:
                                            # If operating on a lazy frame, we won't get the exception until we call .compute()
                                            raise TypeError(
                                                f"Feature `{str(k)}` at index {i} with value '{element}' could not be converted to dtype `{polars_dtype.string_repr()}`"
                                            ) from e
                                elements_as_series.append(element_as_series)
                        elements_as_series = elements_as_series.rechunk(True)
                    else:
                        elements_as_series = pl.Series(name=str(k), values=v)
                    # # Otherwise, we can let polars infer the dtype. We will cast it later if convert_dtypes is True
                    # # We do not want to specify it now, as otherwise polars will drop values instead of cast
                    new_data_dict[str(k)] = elements_as_series
                data = new_data_dict
            data = pl.DataFrame(data)
        if isinstance(data, (pl.LazyFrame, pl.DataFrame)):
            underlying = data
        else:
            raise ValueError(f"Unable to convert data of type {type(data).__name__} into a DataFrame")
        # Rename / validate that all column names are root fqns
        # It is possible that a feature name is a
        self.columns = tuple(Feature.from_root_fqn(str(c)) for c in underlying.columns)
        underlying = underlying.rename(
            {original_c: new_c.root_fqn for (original_c, new_c) in zip(underlying.columns, self.columns)}
        )
        namespaces = [x.path[0].parent.namespace if len(x.path) > 0 else x.namespace for x in self.columns]

        # Convert columns to the correct dtype to match the fqn
        if convert_dtypes:
            for root_fqn in underlying.columns:
                expected_dtype = FEATURE_CODEC.get_polars_dtype(root_fqn)
                actual_dtype = underlying.schema[root_fqn]
                if actual_dtype != expected_dtype:
                    if _polars_dtype_contains_struct(expected_dtype):
                        # Cannot cast to a struct type. Instead, will error, so the user can ensure the underlying
                        # dictionaries / dataclasses are of the correct type
                        raise TypeError(
                            f"Expected field `{root_fqn}` to have dtype `{expected_dtype}`; got dtype `{actual_dtype}`"
                        )
                    else:
                        try:
                            if isinstance(expected_dtype, pl.Datetime) and actual_dtype == pl.Utf8:
                                tzinfo = None if expected_dtype.tz is None else zoneinfo.ZoneInfo(expected_dtype.tz)
                                if expected_dtype.tz is None:
                                    col = (
                                        pl.col(root_fqn)
                                        .apply(
                                            lambda x: None if x is None else _iso_parse(cast(str, x), None),
                                        )
                                        .dt.with_time_zone(None)
                                    )
                                else:
                                    tzinfo = zoneinfo.ZoneInfo(expected_dtype.tz)
                                    col = (
                                        pl.col(root_fqn)
                                        .apply(
                                            lambda x: None if x is None else _iso_parse(cast(str, x), tzinfo),
                                        )
                                        .dt.with_time_zone(expected_dtype.tz)
                                    )
                                underlying = underlying.with_columns([col])
                            else:
                                underlying = underlying.with_columns([pl.col(root_fqn).cast(expected_dtype)])
                        except pl.ComputeError as e:
                            # If operating on a lazy frame, we won't get the exception until we call .compute()
                            raise TypeError(
                                f"Values for feature `{root_fqn}` could not be converted to dtype `{expected_dtype.string_repr()}`. Found type {actual_dtype}, instead."
                            ) from e

        if isinstance(underlying, pl.DataFrame):
            underlying = underlying.lazy()
        self._underlying: pl.LazyFrame = underlying

        # Remove the pseudo-features when determining the namespace
        namespaces_set = set(x for x in namespaces if not x.startswith("__chalk__"))
        if len(namespaces_set) != 1:
            # Allow empty dataframes or dataframes with multiple namespaces
            self.namespace = None
            self.references_feature_set = None
        else:
            self.namespace = get_unique_item(namespaces_set, f"dataframe column namespaces")
            self.references_feature_set = FeatureSetBase.registry[self.namespace]

    ##############
    # Classmethods
    ##############

    @classmethod
    def from_dict(
        cls: Type[TDataFrame],
        data: Dict[Union[str, Feature, FeatureWrapper, Any], Sequence[Any]],
    ) -> TDataFrame:
        warnings.warn(DeprecationWarning("DataFrame.from_dict(...) is deprecated. Instead, use DataFrame(...)"))
        df = cls(data)
        return df

    @overload
    @classmethod
    def from_list(
        cls: Type[TDataFrame],
        data: Sequence[Features],
        /,
    ) -> TDataFrame:
        ...

    @overload
    @classmethod
    def from_list(cls: Type[TDataFrame], *data: Features) -> TDataFrame:
        ...

    @classmethod
    def from_list(cls: Type[TDataFrame], *data: Union[Features, Sequence[Features]]) -> TDataFrame:
        warnings.warn(DeprecationWarning("DataFrame.from_list(...) is deprecated. Instead, use DataFrame(...)"))
        if len(data) == 1 and isinstance(data[0], collections.abc.Sequence):
            # Passed a list as the first argument
            features_seq = data[0]
        else:
            data = cast("Tuple[Features]", data)
            features_seq = data
        df = cls(features_seq)
        return df

    @classmethod
    def read_parquet(
        cls: Type[TDataFrame],
        path: Union[str, pathlib.Path],
        columns: Optional[Union[List[int], List[str], Dict[str, Union[str, Feature, FeatureWrapper, Any]]]] = None,
    ) -> TDataFrame:
        if isinstance(columns, dict):
            columns_to_read = list(columns.keys())
            column_map = {k: str(v) for (k, v) in columns.items()}
        else:
            columns_to_read = columns
            column_map = None
        data = pl.read_parquet(path, columns_to_read)
        if column_map is not None:
            data = data.rename(column_map)
        return cls(data)

    @classmethod
    def read_csv(
        cls: Type[TDataFrame],
        path: Union[str, pathlib.Path],
        has_header: bool,
        columns: Optional[Union[List[int], List[str], Dict[str, Union[str, Feature, FeatureWrapper, Any]]]] = None,
    ) -> TDataFrame:
        if isinstance(columns, dict):
            columns_to_read = list(columns.keys())
            column_map = {k: str(v) for (k, v) in columns.items()}
        else:
            columns_to_read = columns
            column_map = None
        data = pl.read_csv(path, has_header, columns_to_read)
        if column_map is not None:
            data = data.rename(column_map)
        return cls(data)

    #############
    # Aggregation
    #############

    def max(self):
        return DataFrame(self._underlying.max(), convert_dtypes=False)

    def mean(self):
        return DataFrame(self._underlying.mean(), convert_dtypes=False)

    def median(self):
        return DataFrame(self._underlying.median(), convert_dtypes=False)

    def min(self):
        return DataFrame(self._underlying.min(), convert_dtypes=False)

    def std(self, ddof: int = 1):
        return DataFrame(self._underlying.std(ddof), convert_dtypes=False)

    def sum(self):
        # Treat missing sums as zero
        return DataFrame(self._underlying.sum().fill_null(0), convert_dtypes=False)

    def var(self, ddof: int = 1):
        return DataFrame(self._underlying.var(ddof), convert_dtypes=False)

    ####################
    # Summary Operations
    ####################

    # These ops require us to materialize the dataframe.

    def _materialize(self) -> pl.DataFrame:
        materialized = self._underlying.collect()
        self._underlying = materialized.lazy()
        return materialized

    def any(self):
        """Returns whether any of the values in the dataframe are truthy. Requires the dataframe to only contain boolean values."""
        if not all(isinstance(x, type) and issubclass(x, pl.Boolean) for x in self._underlying.dtypes):
            raise TypeError("DataFrame.any() is not defined on a dataframe that contains non-boolean columns.")
        materialized = self._materialize()
        return any(col.any() for col in materialized.get_columns())

    def all(self):
        """Returns whether all of the values in the dataframe are truthy. Requires the dataframe to only contain boolean values."""
        if not all(isinstance(x, type) and issubclass(x, pl.Boolean) for x in self._underlying.dtypes):
            raise TypeError("DataFrame.any() is not defined on a dataframe that contains non-boolean columns.")
        materialized = self._materialize()
        return all(col.all() for col in materialized.get_columns())

    def __len__(self):
        materialized = self._materialize()
        return len(materialized)

    @property
    def shape(self):
        materialized = self._materialize()
        return materialized.shape

    def item(self):
        """Get the only item from the dataframe."""
        materialized = self._materialize()
        if materialized.shape == (1, 1):
            return materialized.rows()[0][0]
        raise ValueError(
            "The dataframe contains multiple items. DataFrame.item() can only be used if the dataframe has a single element."
        )

    def __bool__(self):
        if self.shape == (1, 1):
            # It's a dataframe of 1 item. self.any() and self.all() would return the same thing
            return self.all()
        raise ValueError("__bool__ is ambiguous on a DataFrame. Instead, use DataFrame.any() or DataFrame.all().")

    def __str__(self):
        materialized = self._materialize()
        return str(materialized)

    def __repr__(self):
        materialized = self._materialize()
        return repr(materialized)

    def __float__(self):
        return float(self.item())

    def __int__(self):
        return int(self.item())

    ############################
    # Arithmetic and Comparisons
    ############################

    # These ops require us to materialize the dataframe.

    def _perform_op(
        self,
        op: Callable[[Any, Any], Any],
        other: Union[DataFrame, pl.DataFrame, pd.DataFrame, Any],
        convert_dtypes: bool,
    ):
        materialized = self._materialize()
        if isinstance(other, DataFrame):
            other = other.to_polars()
        if isinstance(other, pl.LazyFrame):
            other = other.collect()
        if isinstance(other, pd.DataFrame):
            other = pl.from_pandas(other)
        return DataFrame(op(materialized, other), convert_dtypes=convert_dtypes)

    def __eq__(self, other: Union[DataFrame, pl.DataFrame, pl.LazyFrame, pd.DataFrame, Any]):  # type: ignore
        return self._perform_op(operator.eq, other, convert_dtypes=False)

    def __ne__(self, other: Union[DataFrame, pl.DataFrame, pl.LazyFrame, pd.DataFrame, Any]):  # type: ignore
        return self._perform_op(operator.ne, other, convert_dtypes=False)

    def __gt__(self, other: Union[DataFrame, pl.DataFrame, pl.LazyFrame, pd.DataFrame, Any]):
        return self._perform_op(operator.gt, other, convert_dtypes=False)

    def __lt__(self, other: Union[DataFrame, pl.DataFrame, pl.LazyFrame, pd.DataFrame, Any]):
        return self._perform_op(operator.lt, other, convert_dtypes=False)

    def __ge__(self, other: Union[DataFrame, pl.DataFrame, pl.LazyFrame, pd.DataFrame, Any]):
        return self._perform_op(operator.ge, other, convert_dtypes=False)

    def __le__(self, other: Union[DataFrame, pl.DataFrame, pl.LazyFrame, pd.DataFrame, Any]):
        return self._perform_op(operator.le, other, convert_dtypes=False)

    def __add__(self, other: Union[DataFrame, pl.DataFrame, pl.LazyFrame, pd.DataFrame, Any]) -> DataFrame:
        return self._perform_op(operator.add, other, convert_dtypes=True)

    def __sub__(self, other: Union[DataFrame, pl.DataFrame, pl.LazyFrame, pd.DataFrame, Any]) -> DataFrame:
        return self._perform_op(operator.sub, other, convert_dtypes=True)

    def __mul__(self, other: Union[int, float]) -> DataFrame:
        return self._perform_op(operator.mul, other, convert_dtypes=True)

    def __truediv__(self, other: Union[int, float]) -> DataFrame:
        return self._perform_op(operator.truediv, other, convert_dtypes=True)

    def __floordiv__(self, other: Union[int, float]) -> DataFrame:
        return self._perform_op(operator.floordiv, other, convert_dtypes=True)

    def __mod__(self, other: Union[int, float]) -> DataFrame:
        return self._perform_op(operator.mod, other, convert_dtypes=True)

    def __pow__(self, other: Union[int, float]) -> DataFrame:
        return self._perform_op(operator.pow, other, convert_dtypes=True)

    ############
    # Conversion
    ############
    def to_polars(self) -> pl.LazyFrame:
        """Get the underlying dataframe as a Polars LazyFrame."""
        # Implementing to_polars() to return the LazyFrame, rather than the DataFrame, to encourage customers to use
        # lazy operations if possible. They can manually call .collect() if needed
        return self._underlying

    def to_pandas(self) -> pd.DataFrame:
        """Get the underlying dataframe as a Pandas DataFrame."""
        # For pandas, the columns should be the Features, not the root fqns
        def types_mapper(dtype: pyarrow.DataType):
            if dtype in (pyarrow.utf8(), pyarrow.large_utf8()):
                return pd.StringDtype()
            return None

        pd_dataframe = self._underlying.collect().to_pandas(types_mapper=types_mapper)
        pd_dataframe.columns = pd_dataframe.columns.astype("object")
        pd_dataframe = pd_dataframe.rename(columns={x.root_fqn: x for x in self.columns})
        return pd_dataframe

    #######################
    # Filtering / Selecting
    #######################
    def __getitem__(self, item: Any):
        from chalk.features.feature_set import FeatureSetBase

        has_bool_or_filter_value = any(isinstance(x, (bool, Filter)) for x in ensure_tuple(item))
        if has_bool_or_filter_value:
            # If we have a boolean or Filter value, then that means we need to ast-parse the caller since
            # python has already evaluated AND, OR, and IN operations into literal booleans or Filters
            # Skipping the parsing unless if we have need to for efficiency and to eliminate conflicts
            # with pytest
            from chalk.df.ast_parser import parse_dataframe_getitem

            item = parse_dataframe_getitem()
        if any(isinstance(x, (FeatureWrapper, Feature, Filter)) for x in ensure_tuple(item)):
            # Use the Chalk projection / selection syntax, where we support our Filter objects and
            # selection by column name
            projections: list[str] = []
            filters: List[Filter] = []
            for x in ensure_tuple(item):
                if isinstance(x, (FeatureWrapper, Feature, str)):
                    projections.append(str(x))

                elif isinstance(x, Filter):
                    filters.append(x)
                else:
                    raise TypeError(
                        "When indexing by Filters or Features, it is not simultaneously possible to perform other indexing operations."
                    )

            now = datetime.datetime.now(tz=datetime.timezone.utc)
            timestamp_feature = None if self.namespace is None else FeatureSetBase.registry[self.namespace].__chalk_ts__
            pl_expr = convert_filters_to_pl_expr(filters, self._underlying.schema, timestamp_feature, now)
            df = self._underlying
            if pl_expr is not None:
                df = df.filter(pl_expr)
            # Do the projection
            if len(projections) > 0:
                df = df.select(projections)
            return DataFrame(df)
        else:
            # Otherwise, use the standard polars selection format
            # Must materialize the dataframe to use __getitem__
            materialized = self._materialize()
            df = materialized[item]
            return DataFrame(df)


def _feature_type_or_value(e: Union[Feature, FeatureWrapper]):
    if isinstance(e, FeatureWrapper):
        e = unwrap_feature(e)
    return e


def _polars_dtype_contains_struct(dtype: pl.DataType | Type[pl.DataType]):
    """Returns whether the dtype contains a (potentially nested) struct"""
    if isinstance(dtype, pl.Struct) or (isinstance(dtype, type) and issubclass(dtype, pl.Struct)):
        return True
    if isinstance(dtype, pl.List):
        assert dtype.inner is not None
        return _polars_dtype_contains_struct(dtype.inner)
    return False


def _maybe_replace_timestamp_feature(f: Union[Feature, Any], observed_at_feature: Optional[Feature]):
    """Replace the ``CHALK_TS`` pseudo-feature with the actual timestamp column."""
    if not isinstance(f, Feature) or f.fqn != "__chalk__.CHALK_TS":
        return f
    if observed_at_feature is not None:
        return observed_at_feature
    raise ValueError("No Timestamp Feature Found")


def _maybe_convert_timedelta_to_timestamp(
    f: Union[TimeDelta, datetime.timedelta, Any], now: Optional[datetime.datetime]
):
    """Convert timedeltas relative to ``now`` into absolute datetimes."""
    if isinstance(f, TimeDelta):
        f = f.to_std()
    if isinstance(f, datetime.timedelta):
        if now is None:
            raise ValueError(
                "The filter contains a relative timestamp. The current datetime must be provided to evaluate this filter."
            )
        return now + f
    return f


def _parse_feature_or_value(
    f: Union[Feature, Any], timestamp_feature: Optional[Feature], now: Optional[datetime.datetime]
):
    """Parse a feature or value into the correct type that can be used for filtering."""
    f = _feature_type_or_value(f)
    f = _maybe_convert_timedelta_to_timestamp(f, now)
    f = _maybe_replace_timestamp_feature(f, timestamp_feature)
    if isinstance(f, enum.Enum):
        f = f.value
    return f


def _polars_is_eq(
    lhs: Any,
    rhs: Any,
    lhs_dtype: Optional[Union[Type[pl.DataType], pl.DataType]],
    rhs_dtype: Optional[Union[Type[pl.DataType], pl.DataType]],
):
    """Compare a column with another column or literal value, including possibly a struct.
    Polars does not permit equality comparisons on structs directly. Instead, must compare field by field, potentially recursively.
    """
    if rhs_dtype is not None:
        if lhs_dtype is None:
            # Swap the columns
            return _polars_is_eq(rhs, lhs, rhs_dtype, lhs_dtype)
        else:
            # Comparing two columns
            assert isinstance(lhs, pl.Expr)
            assert isinstance(rhs, pl.Expr)
            if isinstance(lhs_dtype, pl.Struct):
                assert isinstance(rhs_dtype, pl.Struct)
                # Assert equality field by field
                filters = []
                for field in lhs_dtype.fields:
                    field_name = field.name
                    new_lhs = lhs.struct.field(field_name)
                    new_lhs_dtype = field.dtype
                    new_rhs = rhs.struct.field(field_name)
                    new_rhs_dtype = field.dtype
                    filters.append(_polars_is_eq(new_lhs, new_rhs, new_lhs_dtype, new_rhs_dtype))
                assert len(filters) > 0, "structs with 0 fields are unsupported"
                return functools.reduce(lambda a, b: a & b, filters)
            return lhs == rhs
    # rhs is literal
    # lhs is a column
    assert lhs_dtype is not None, "one side must be a column"
    assert isinstance(lhs, pl.Expr)
    if isinstance(lhs_dtype, pl.Struct):
        # Assert equality field by field
        filters = []
        for field in lhs_dtype.fields:
            field_name = field.name
            new_lhs = lhs.struct.field(field_name)
            new_lhs_dtype = field.dtype
            # Assuming that struct-like objects make their members accessible by attribute name or __getitem__
            try:
                new_rhs = getattr(rhs, field_name)
            except AttributeError:
                new_rhs = rhs[field_name]
            new_rhs_dtype = None  # literal values do not have dtypes
            filters.append(_polars_is_eq(new_lhs, new_rhs, new_lhs_dtype, new_rhs_dtype))
        assert len(filters) > 0, "structs with 0 fields are unsupported"
        return functools.reduce(lambda a, b: a & b, filters)
    if not isinstance(lhs_dtype, type):
        lhs_dtype = type(lhs_dtype)
    return lhs == pl.lit(rhs, dtype=lhs_dtype, allow_object=True)


def _polars_is_in(lhs: pl.Expr, rhs: Iterable, lhs_dtype: Union[Type[pl.DataType], pl.DataType]):
    """Filter for where the lhs is in the RHS. The RHS must be a literal collection."""
    if isinstance(lhs_dtype, pl.Struct):
        # Assert equality field by field
        filters = []
        rhs_by_fields: Dict[str, List[Any]] = {}
        for item in rhs:
            for field in lhs_dtype.fields:
                if field.name not in rhs_by_fields:
                    rhs_by_fields[field.name] = []
                # Assuming that struct-like objects make their members accessible by attribute name or __getitem__
                try:
                    rhs_vector = getattr(item, field.name)
                except AttributeError:
                    rhs_vector = item[field.name]
                rhs_by_fields[field.name].append(rhs_vector)
        for field in lhs_dtype.fields:
            field_name = field.name
            new_lhs = lhs.struct.field(field_name)
            new_lhs_dtype = field.dtype
            new_rhs = rhs_by_fields[field_name]
            filters.append(_polars_is_in(new_lhs, new_rhs, new_lhs_dtype))
        assert len(filters) > 0, "structs with 0 fields are unsupported"
        return functools.reduce(lambda a, b: a & b, filters)
    if not isinstance(lhs_dtype, type):
        lhs_dtype = type(lhs_dtype)
    return lhs.is_in(pl.lit(pl.Series(values=rhs, dtype=lhs_dtype), allow_object=True))


def _coerce_value_to_dtype(val: Any, dtype: Union[pl.DataType, Type[pl.DataType]]):
    # For the most part, we don't need to do any manual coercion -- polars will handle that for us.
    # Only need to pay attention to enums, which could be stored as the underlying type, or as an object
    if isinstance(val, collections.abc.Iterable) and not isinstance(val, str):
        return [_coerce_value_to_dtype(x, dtype) for x in val]
    if isinstance(val, enum.Enum) and dtype != pl.Object:
        return val.value
    return val


def _convert_filter_to_pl_expr(
    f: Filter,
    df_schema: dict[str, pl.PolarsDataType],
    timestamp_feature: Optional[Feature] = None,
    now: Optional[datetime.datetime] = None,
) -> pl.Expr:
    """Convert filters to a polars expression

    Args:
        f: The filter
        df_schema: The DataFrame schema.
        timestamp_feature: The feature corresponding to the observation time
        now: The datetime to use for the current timestamp. Used to resolve relative
            timestamps in filters to absolute datetimes.

    Returns:
        A series of boolean values that can be used to select the rows where the filter is truthy
    """
    # Passing `now` in explicitly instead of using datetime.datetime.now() so that multiple filters
    # relying on relative timestamps (e.g. before, after) will have the same "now" time.
    if f.operation == "not":
        assert f.rhs is None, "not has just one side"
        assert isinstance(f.lhs, Filter), "lhs must be a filter"
        return ~_convert_filter_to_pl_expr(f.lhs, df_schema, timestamp_feature, now)
    elif f.operation == "and":
        assert isinstance(f.rhs, Filter), "rhs must be a filter"
        assert isinstance(f.lhs, Filter), "lhs must be a filter"
        return _convert_filter_to_pl_expr(f.lhs, df_schema, timestamp_feature, now) & _convert_filter_to_pl_expr(
            f.rhs, df_schema, timestamp_feature, now
        )
    elif f.operation == "or":
        assert isinstance(f.rhs, Filter), "rhs must be a filter"
        assert isinstance(f.lhs, Filter), "lhs must be a filter"
        return _convert_filter_to_pl_expr(f.lhs, df_schema, timestamp_feature, now) | _convert_filter_to_pl_expr(
            f.rhs, df_schema, timestamp_feature, now
        )

    lhs = _parse_feature_or_value(f.lhs, timestamp_feature, now)
    rhs = _parse_feature_or_value(f.rhs, timestamp_feature, now)

    lhs_dtype = None
    if isinstance(lhs, Feature):
        lhs_dtype = df_schema[str(lhs)]
        lhs = pl.col(str(lhs))

    rhs_dtype = None
    if isinstance(rhs, Feature):
        rhs_dtype = df_schema[str(rhs)]
        rhs = pl.col(str(rhs))

    if lhs_dtype is None:
        # LHS is literal. Encode it into the rhs_dtype
        assert rhs_dtype is not None
        lhs = _coerce_value_to_dtype(lhs, rhs_dtype)
    if rhs_dtype is None:
        # RHS is literal. Encode it into the lhs_dtype
        assert lhs_dtype is not None
        rhs = _coerce_value_to_dtype(rhs, lhs_dtype)

    if rhs is None:
        assert isinstance(lhs, pl.Expr)
        if f.operation == "==":
            return lhs.is_null()

        elif f.operation == "!=":
            return lhs.is_not_null()

    if f.operation in ("in", "not in"):
        assert lhs_dtype is not None
        assert isinstance(lhs, pl.Expr)
        assert isinstance(rhs, collections.abc.Iterable)
        ret = _polars_is_in(lhs, rhs, lhs_dtype)
        if f.operation == "not in":
            ret = ~ret
    elif f.operation in ("==", "!="):
        ret = _polars_is_eq(lhs, rhs, lhs_dtype, rhs_dtype)
        if f.operation == "!=":
            ret = ~ret
    elif f.operation == "!=":
        ret = lhs != rhs
    elif f.operation == ">=":
        ret = lhs >= rhs  # type: ignore
    elif f.operation == ">":
        ret = lhs > rhs  # type: ignore
    elif f.operation == "<":
        ret = lhs < rhs  # type: ignore
    elif f.operation == "<=":
        ret = lhs <= rhs  # type: ignore
    else:
        raise ValueError(f'Unknown operation "{f.operation}"')
    assert isinstance(ret, pl.Expr)
    return ret


def convert_filters_to_pl_expr(
    filters: Sequence[Filter],
    df_schema: dict[str, pl.PolarsDataType],
    timestamp_feature: Optional[Feature] = None,
    now: Optional[datetime.datetime] = None,
):
    if len(filters) == 0:
        return None
    polars_filters = (_convert_filter_to_pl_expr(f, df_schema, timestamp_feature, now) for f in filters)
    return functools.reduce(lambda a, b: a & b, polars_filters)


def _generate_empty_series_for_dtype(name: str, dtype: Union[Type[pl.DataType], pl.DataType], length: int) -> pl.Series:
    """Safely generate a series of all null values for the specified datatype.

    Unlike the ``pl.Series`` constructor, this function can handle struct dtypes.
    """
    if isinstance(dtype, pl.Struct):
        # Struct dtypes cannot be specified in the pl.Series constructor.
        # Instead, create a dataframe, then call .to_struct() on it
        # If recursing within a struct, it should have a length of zero
        data = {f.name: _generate_empty_series_for_dtype(f.name, f.dtype, length) for f in dtype.fields}
        temp_df = pl.DataFrame(data)
        return temp_df.to_struct(name)
    if isinstance(dtype, pl.List):
        assert dtype.inner is not None
        data = {name: _generate_empty_series_for_dtype(name, dtype.inner, 0)}
        temp_df = pl.DataFrame(data)
        list_of_struct_series = temp_df.select(pl.col(name).reshape((length, -1))).get_column(name)
        return list_of_struct_series
    return pl.Series(name, dtype=dtype, values=([None] * length))


# list [[], [None, None]]


def _preprocess_element(element: Any):
    if isinstance(element, enum.Enum):
        element = element.value
    # Polars has trouble with third-party timezone libraries,
    # So convert it to python's internal timezone library
    if isinstance(element, datetime.datetime) and element.tzinfo is not None:
        element = element.astimezone(datetime.timezone.utc)
    return element
