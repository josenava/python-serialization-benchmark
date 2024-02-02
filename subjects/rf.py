from django.conf import settings

from data import ValidatedTestObject

settings.configure()

import django
django.setup()

from rest_framework import serializers as rf_serializers

name = 'Django REST Framework'


class SubRF(rf_serializers.Serializer):
    w = rf_serializers.IntegerField()
    x = rf_serializers.SerializerMethodField()
    y = rf_serializers.CharField()
    z = rf_serializers.IntegerField()

    def get_x(self, obj):
        return obj.x + 10


class ComplexRF(rf_serializers.Serializer):
    foo = rf_serializers.CharField()
    bar = rf_serializers.IntegerField()
    sub = SubRF()
    subs = SubRF(many=True)


class ComplexRFValidator(rf_serializers.Serializer):
    id_ = rf_serializers.UUIDField(source="id")
    start_date = rf_serializers.DateField(input_formats=["%Y-%m-%d"])
    end_date = rf_serializers.DateField(input_formats=["%Y-%m-%d"])

    def validate(self, data):
        if data["start_date"] > data["end_date"]:
            raise rf_serializers.ValidationError("Start date cannot be greater than end date")
        return data

    def build_dto(self) -> ValidatedTestObject:
        return ValidatedTestObject(
            self.validated_data["id"],
            self.validated_data["start_date"],
            self.validated_data["end_date"]
        )


def serialize_func(obj, many):
    return ComplexRF(obj, many=many).data


def deserialize_func(obj, many):
    validator = ComplexRFValidator(data=obj, many=many)
    validator.is_valid(raise_exception=True)
    if many:
        return [
            ValidatedTestObject(
                valid_["id"],
                valid_["start_date"],
                valid_["end_date"],
            ) for valid_ in validator.validated_data
        ]
    return validator.build_dto()
