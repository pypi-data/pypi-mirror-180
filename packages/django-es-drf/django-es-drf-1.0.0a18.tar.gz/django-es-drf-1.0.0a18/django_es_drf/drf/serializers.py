from typing import Type

from rest_framework.exceptions import ValidationError
from rest_framework.fields import empty
from rest_framework.serializers import (
    BaseSerializer,
    Serializer,
    ModelSerializer,
    as_serializer_error,
)
from rest_framework.utils.serializer_helpers import ReturnDict
import elasticsearch_dsl as e


class StrictModelSerializer(ModelSerializer):
    def run_validation(self, data=empty):
        validated_data = super().run_validation(data)

        if data is not empty:
            data_keys = set(data.keys())
            validated_keys = set(validated_data.keys())

            for fld in self.fields.values():
                if fld.read_only and fld.field_name in data_keys:
                    data_keys.remove(fld.field_name)

            if data_keys != validated_keys:
                raise ValidationError(
                    detail=as_serializer_error(
                        ValidationError(f"Unexpected keys {data_keys - validated_keys}")
                    )
                )
        return validated_data


class ESDocumentSerializer(BaseSerializer):
    django_serializer: Type[Serializer]

    def __init__(self, *args, django_serializer=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.django_serializer = django_serializer

    def to_internal_value(self, data):
        serializer = self.django_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        if hasattr(serializer, "document_data"):
            return serializer.document_data
        return serializer.validated_data

    def to_representation(self, instance):
        # just return the document
        return instance

    def create(self, validated_data):
        document_class = self.context["view"].document
        # TODO: nested are not supported
        doc = document_class(**validated_data)
        doc.save()
        return doc

    def update(self, instance, validated_data):
        if self.partial:
            for k, v in validated_data.items():
                setattr(instance, k, v)
        else:
            # clear the instance
            doctype = type(instance)
            if doctype.DOCUMENT_ID_FIELD not in validated_data:
                validated_data[doctype.DOCUMENT_ID_FIELD] = instance.meta.id
            if not self.partial:
                _mapping = instance._doc_type.mapping
                for fld_name in _mapping:
                    fld = _mapping[fld_name]
                    if fld_name not in validated_data:
                        if fld._multi:
                            validated_data[fld_name] = []
                        elif isinstance(fld, e.Object):
                            validated_data[fld_name] = {}
                        else:
                            validated_data[fld_name] = None
            instance = doctype(meta={"id": instance.meta.id}, **validated_data)
        instance.save()
        return instance

    def get_initial(self):
        return super().get_initial() or {}

    @property
    def fields(self):
        return self.django_serializer().fields

    @property
    def data(self):
        ret = super().data
        if isinstance(ret, dict):
            return ReturnDict(ret, serializer=self)
        else:
            return ret

    def __iter__(self):
        # TODO: implement this to get better support for DRF debug interface
        return iter([])
