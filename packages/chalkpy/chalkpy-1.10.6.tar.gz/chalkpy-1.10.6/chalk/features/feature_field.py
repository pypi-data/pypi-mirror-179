from __future__ import annotations

import copy
import dataclasses
import functools
import itertools
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Any, Callable, List, Optional, Tuple, Type, TypeVar, Union, cast

import polars as pl

from chalk.features.tag import Tags
from chalk.serialization.parsed_annotation import ParsedAnnotation
from chalk.utils.collections import ensure_tuple
from chalk.utils.duration import Duration, timedelta_to_duration

if TYPE_CHECKING:
    from chalk.features.feature_set import Features
    from chalk.features.filter import Filter

T = TypeVar("T")
U = TypeVar("U")
JsonValue = TypeVar("JsonValue")

__all__ = ["Feature", "feature", "feature_time", "has_one", "has_many"]


@dataclasses.dataclass
class HasOnePathObj:
    parent: Feature
    child: Feature
    parent_to_child_attribute_name: str


@dataclasses.dataclass
class FeatureValidation:
    min: Optional[T]
    max: Optional[T]
    min_length: Optional[int]
    max_length: Optional[int]
    contains: Optional[T]


class Feature:
    def __init__(
        self,
        name: Optional[str] = None,
        attribute_name: Optional[str] = None,
        namespace: Optional[str] = None,
        features_cls: Optional[Type[Features]] = None,
        typ: Optional[Union[ParsedAnnotation, type]] = None,
        version: Optional[int] = None,
        description: Optional[str] = None,
        owner: Optional[str] = None,
        tags: Optional[List[str]] = None,
        primary: bool = False,
        max_staleness: Optional[Duration] = ...,
        etl_offline_to_online: Optional[bool] = None,
        encoder: Optional[Callable[[Any], JsonValue]] = None,
        decoder: Optional[Callable[[JsonValue], Any]] = None,
        polars_dtype: Optional[Union[Type[pl.DataType], pl.DataType]] = None,
        join: Optional[Union[Callable[[], Filter], Filter]] = None,
        path: Tuple[HasOnePathObj, ...] = (),
        is_feature_time: bool = False,
        is_autogenerated: bool = False,
        validations: Optional[FeatureValidation] = None,
    ):
        self.typ = ParsedAnnotation(underlying=typ) if isinstance(typ, type) else typ
        self.features_cls = features_cls
        self._name = name
        # the attribute name for the feature in the @features class (in case if the name is specified differently)
        self._attribute_name = attribute_name
        self._namespace = namespace
        self.path = path
        self.version = version
        self.description = description
        self.owner = owner
        self.tags = tags
        self.primary = primary
        self.max_staleness = max_staleness
        self.etl_offline_to_online = etl_offline_to_online
        self.encoder = encoder
        self.decoder = decoder
        self.polars_dtype = polars_dtype
        self.is_feature_time = is_feature_time
        self.is_autogenerated = is_autogenerated
        self._join = join
        self._validations = validations

    def __str__(self):
        return self.root_fqn

    @property
    def attribute_name(self):
        if self._attribute_name is None:
            raise RuntimeError(
                "Feature.attribute_name is not yet defined. Is the feature being constructed outside of a Features class?"
            )
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name: str):
        self._attribute_name = attribute_name
        if self._name is None:
            # If there is no name, also set the name to the attribute name
            self._name = attribute_name

    @property
    def name(self):
        if self._name is None:
            raise RuntimeError(
                "Feature.name is not yet defined. Is the feature being constructed outside of a Features class?"
            )
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def namespace(self):
        if self._namespace is None:
            raise RuntimeError(
                "Feature.namespace is not yet defined. Is the feature being constructed outside of a Features class?"
            )
        return self._namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self._namespace = namespace

    @classmethod
    @functools.lru_cache(1024)
    def from_root_fqn(cls, root_fqn: str) -> Feature:
        """Convert a Root FQN into a feature.

        Args:
            root_fqn: The root fqn of the feature

        Returns:
            The feature for that root_fqn.
        """
        from chalk.features.feature_set import Features, FeatureSetBase
        from chalk.features.pseudofeatures import PSEUDOFEATURES

        for x in PSEUDOFEATURES:
            if root_fqn == x.root_fqn or root_fqn == x.name:
                return x
        split_fqn = root_fqn.split(".")
        root_ns = split_fqn[0]
        split_fqn = split_fqn[1:]
        features_cls = FeatureSetBase.registry[root_ns]

        # FQNs are by name, so must lookup the feature in features_cls.features instead of using getattr
        feat: Optional[Feature] = None

        while len(split_fqn) > 0:
            feature_name = split_fqn[0]
            split_fqn = split_fqn[1:]

            found_feature = False

            for x in features_cls.features:
                assert isinstance(x, Feature)
                if x.name == feature_name:
                    assert x.attribute_name is not None
                    found_feature = True
                    feat = x if feat is None else feat.copy_with_path(x)
                    if len(split_fqn) > 0:
                        # Going to recurse, so validate that the feature is something that we can recurse on.
                        if not x.is_has_one:
                            raise TypeError(
                                (
                                    f"Feature {features_cls.__chalk_namespace__}.{feature_name}.{'.'.join(split_fqn)} "
                                    f"does not exist as {features_cls.__chalk_namespace__}.{feature_name} "
                                    f"is not a has-one"
                                )
                            )
                        assert x.typ is not None
                        assert issubclass(x.typ.underlying, Features)
                        features_cls = x.typ.underlying
                    break
            if not found_feature:
                raise ValueError(
                    f"Did not find feature named '{feature_name}' in features cls {features_cls.__chalk_namespace__}"
                )
        assert feat is not None
        return feat

    @property
    def root_namespace(self) -> str:
        if len(self.path) > 0:
            assert self.path[0].parent.namespace is not None, "parent namespace is None"
            return self.path[0].parent.namespace
        assert self.namespace is not None, "namespace is None"
        return self.namespace

    @property
    def root_fqn(self):
        assert self.name is not None, "Missing name on feature"
        if len(self.path) > 0:
            return ".".join(
                itertools.chain(
                    (self.root_namespace,),
                    (x.parent.name for x in self.path),
                    (self.name,),
                )
            )
        return f"{self.namespace}.{self.name}"

    def __hash__(self) -> int:
        return hash(self.root_fqn)

    def __eq__(self, other: object):
        if self.is_has_many:
            # For equality checks on a has-many, we would also need to compare the columns and types
            # For now, ignoring.
            return NotImplemented
        if isinstance(other, Feature):
            other = other.root_fqn
        if isinstance(other, str):
            return self.root_fqn == other
        return NotImplemented

    def __repr__(self):
        return f"Feature(fqn={self.namespace}.{self.name}, typ={self.typ})"

    @property
    def fqn(self) -> str:
        return f"{self.namespace}.{self.name}"

    @property
    def is_has_one(self):
        # A feature is a has-one relationship if the type is
        # another singleton features cls and there is a join condition
        assert self.typ is not None
        # Need to short-circuit if it is a dataframe, as DataFrames
        # might not have an underlying
        return not self.typ.is_dataframe and self.join is not None

    @property
    def is_has_many(self):
        assert self.typ is not None
        return self.typ.is_dataframe and self.join is not None

    @property
    def is_scalar(self):
        return not self.is_has_many and not self.is_has_one and not self.is_feature_time

    @property
    def has_resolved_join(self):
        return self._join is not None

    @property
    def join(self) -> Optional[Filter]:
        from chalk.features.feature_set import Features

        if self._join is not None:
            # Join was explicitly specified
            return self._join() if callable(self._join) else self._join
        # Attempt to extract the join condition from the foreign feature
        assert self.typ is not None
        foreign_features = self.typ.underlying
        if not issubclass(foreign_features, Features):
            return None
        assert self.features_cls is not None
        joins: List[Tuple[str, Filter]] = []  # Tuple of (name, Join)
        for f in foreign_features.features:
            assert isinstance(f, Feature)
            assert f.typ is not None
            if f.typ.underlying is self.features_cls and f.has_resolved_join:
                assert f.join is not None
                assert f.name is not None
                join = f.join() if callable(f.join) else f.join
                joins.append((f.name, join))
        if len(joins) == 0:
            # It's a nested feature
            return None
        # TODO(Ravi): Enable this check. But let's see if we can be smarter about which join to automatically use, if there are multiple
        # if len(joins) > 1:
        #     assert self.features_cls is not None
        #     raise ValueError(
        #         f"Multiple join conditions exist for {self.features_cls.__name__} and {foreign_features.__name__} on keys: "
        #         + f", ".join(f'{foreign_features.__name__}.{name}' for (name, _) in joins)
        #     )
        join = joins[0][1]
        if callable(join):
            join = join()
        self._join = join
        return join

    @property
    def joined_class(self) -> Optional[Type[Features]]:
        j = self.join
        if j is None:
            return None
        if j.lhs is not None and j.rhs is not None and isinstance(j.lhs, Feature) and isinstance(j.rhs, Feature):
            if j.lhs.namespace != self.namespace:
                return j.lhs.features_cls
            return j.rhs.features_cls
        return None

    def copy_with_path(self, child: Feature) -> Feature:
        child_copy = copy.copy(child)
        assert child.attribute_name is not None
        child_copy.path = tuple(
            (
                *self.path,
                HasOnePathObj(
                    parent=self,
                    child=child,
                    parent_to_child_attribute_name=child.attribute_name,
                ),
            )
        )
        return child_copy


def feature(
    description: Optional[str] = None,
    owner: Optional[str] = None,
    tags: Optional[Tags] = None,
    name: Optional[str] = None,
    version: Optional[int] = None,
    primary: bool = False,
    max_staleness: Optional[Duration] = ...,
    etl_offline_to_online: Optional[bool] = None,
    encoder: Optional[Callable[[T], JsonValue]] = None,
    decoder: Optional[Callable[[JsonValue], T]] = None,
    min: Optional[T] = None,
    max: Optional[T] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    contains: Optional[T] = None,
    dtype: Optional[Union[Type[pl.DataType], pl.DataType]] = None,
) -> T:
    return cast(
        T,
        Feature(
            name=name,
            version=version,
            owner=owner,
            tags=None if tags is None else list(ensure_tuple(tags)),
            description=description,
            primary=primary,
            max_staleness=timedelta_to_duration(max_staleness)
            if isinstance(max_staleness, timedelta)
            else max_staleness,
            etl_offline_to_online=etl_offline_to_online,
            encoder=encoder,
            decoder=decoder,
            polars_dtype=dtype,
            validations=FeatureValidation(
                min=min,
                max=max,
                min_length=min_length,
                max_length=max_length,
                contains=contains,
            ),
        ),
    )


def feature_time() -> Any:
    return Feature(typ=datetime, is_feature_time=True)


def has_one(f: Callable[[], Any]) -> Any:
    return Feature(join=f)


def has_many(f: Callable[[], Any]) -> Any:
    return Feature(join=f)
