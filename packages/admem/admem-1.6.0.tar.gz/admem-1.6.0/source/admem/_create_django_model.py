# Copyright (c) 2022 Mario S. Könz; License: MIT
import dataclasses as dc
import datetime
import enum
import types
import typing as tp
from pathlib import Path

from django.db import models

from ._decorator import BACKEND_LINKER
from ._util import public_name

__all__ = ["CreateDjangoModel", "create_django_model"]


@dc.dataclass(frozen=True)
class InspectDataclass:
    dataclass: type

    def extract_meta(
        self,
    ) -> tuple[
        str | None,
        list[str] | None,
        dict[str, dict[str, tp.Any]] | None,
        list[str] | None,
    ]:
        pk_key, unique_together, extra_kwgs, ordering = None, None, None, None
        if hasattr(self.dataclass, "Meta"):
            meta = self.dataclass.Meta  # type: ignore
            if hasattr(meta, "primary_key"):
                pk_key = meta.primary_key
                assert isinstance(pk_key, str)
            if hasattr(meta, "unique_together"):
                unique_together = meta.unique_together
                assert isinstance(unique_together, list)
            if hasattr(meta, "extra"):
                extra_kwgs = meta.extra
                assert isinstance(extra_kwgs, dict)
            if hasattr(meta, "ordering"):
                ordering = meta.ordering
                assert isinstance(ordering, list)

        return pk_key, unique_together, extra_kwgs, ordering

    def get_identifying_parameter(self) -> set[str]:
        pk_key, unique_together, _, _ = self.extract_meta()
        res = set()
        if pk_key is not None:
            res.add(pk_key)
        if unique_together is not None:
            res.update(unique_together)
        return res


@dc.dataclass(frozen=True)
class CreateDjangoModel(InspectDataclass):
    def __post_init__(self) -> None:
        # evaluate the Meta class
        pk_key, unique_together, extra_kwgs, ordering = self.extract_meta()
        # translate fields
        fields: dict[str, tp.Any] = self.translate_fields(pk_key, extra_kwgs)
        fields["Meta"] = self.generate_meta(unique_together, ordering)
        # pylint: disable=comparison-with-callable
        if self.dataclass.__str__ != object.__str__:  # type: ignore
            fields["__str__"] = self.dataclass.__str__
        fields["__module__"] = fields["Meta"].app_label
        django_model = type(self.dataclass.__name__, (models.Model,), fields)
        BACKEND_LINKER.link(self.dataclass, django_model)

    def translate_fields(
        self, pk_key: str | None, extra_kwgs: dict[str, dict[str, tp.Any]] | None
    ) -> "dict[str, models.Field[tp.Any, tp.Any]]":
        fields = {}
        for field in dc.fields(self.dataclass):
            django_field, opts = self.django_field_precursor(field.type)
            if field.name == pk_key:
                opts["primary_key"] = True
                if django_field is models.ForeignKey:
                    django_field = models.OneToOneField
            default = self.get_default(field)
            if default:
                opts["default"] = default
            extra = {}
            if extra_kwgs:
                extra = extra_kwgs.pop(field.name, {})
            fields[field.name] = django_field(**opts, **extra)
        if extra_kwgs:
            raise RuntimeError(
                f"unconsumed extra kwgs ({extra_kwgs}) found for {self.dataclass}, please adjust!"
            )
        return fields

    def generate_meta(
        self, unique_together: list[str] | None, ordering: list[str] | None
    ) -> type:
        class Meta:
            app_label = public_name(self.dataclass, without_cls=True)
            db_table = public_name(self.dataclass)

        if unique_together:
            Meta.unique_together = unique_together  # type: ignore

        if ordering:
            Meta.ordering = ordering  # type: ignore

        return Meta

    @classmethod
    def django_field_precursor(
        cls, type_: type
    ) -> "tuple[type[models.Field[tp.Any, tp.Any]], dict[str, tp.Any]]":
        # pylint: disable=too-many-return-statements,too-many-branches
        if type_ == str:
            return models.CharField, dict(max_length=1024)
        if type_ == int:
            return models.IntegerField, {}
        if type_ == float:
            return models.FloatField, {}
        if type_ == datetime.datetime:
            return models.DateTimeField, {}
        if type_ == datetime.date:
            return models.DateField, {}
        if type_ == datetime.time:
            return models.TimeField, {}
        if type_ == bytes:
            return models.BinaryField, dict(editable=True)
        if type_ == bool:
            return models.BooleanField, {}

        if isinstance(type_, types.GenericAlias):
            origin = tp.get_origin(type_)
            subtypes = tp.get_args(type_)
            if origin is set:
                assert len(subtypes) == 1
                subtype = subtypes[0]
                try:
                    fk_class = BACKEND_LINKER.backend_class(subtype)
                    assert issubclass(fk_class, models.Model)
                    return models.ManyToManyField, dict(to=fk_class, related_name="+")
                except KeyError:
                    pass

        if isinstance(type_, types.UnionType):
            target_type, none_type = tp.get_args(type_)
            if none_type is type(None):
                field, kwgs = cls.django_field_precursor(target_type)
                kwgs["blank"] = True
                kwgs["null"] = True
                return field, kwgs

        if issubclass(type_, enum.Enum):
            max_length = 256
            choices = []
            for val in type_.__members__.values():
                choices.append((val.value, val.value))
                assert len(val.value) < max_length

            return models.CharField, dict(max_length=max_length, choices=choices)

        if issubclass(type_, Path):
            return models.FileField, dict(max_length=255)

        try:  # try Foreign Key relation (many-to-one)
            fk_class = BACKEND_LINKER.backend_class(type_)
            assert issubclass(fk_class, models.Model)
            return models.ForeignKey, dict(
                to=fk_class, on_delete=models.CASCADE, related_name="+"
            )

        except KeyError:
            pass

        raise NotImplementedError(type_)

    @classmethod
    def get_default(cls, field: dc.Field[tp.Any]) -> tp.Any:
        if field.default != dc.MISSING:
            assert field.default_factory is dc.MISSING
            return field.default
        if field.default_factory != dc.MISSING:
            assert field.default is dc.MISSING
            return field.default_factory
        return None


def create_django_model(dataclass: type) -> type:
    CreateDjangoModel(dataclass)
    return dataclass
