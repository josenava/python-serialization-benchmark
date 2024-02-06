from datetime import date
from typing import Self, Annotated
from uuid import UUID

import pydantic
from pydantic import Field, model_validator, AfterValidator

from data import ValidatedTestObject

name = "Pydantic"


class SubP(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(from_attributes=True)

    w: int
    x: Annotated[int, AfterValidator(lambda x: x + 10)]
    y: str
    z: int


class ComplexP(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(from_attributes=True)

    bar: int
    foo: str
    sub: SubP
    subs: list[SubP]


class ComplexPValidator(pydantic.BaseModel):
    id: UUID = Field(validation_alias="id_")
    start_date: date
    end_date: date

    @model_validator(mode="after")
    def validate_dates(self) -> Self:
        if self.start_date > self.end_date:
            raise ValueError("Start date cannot be greater than end date")
        return self

    def build_dto(self) -> Self:
        return ValidatedTestObject(
            self.id,
            self.start_date,
            self.end_date,
        )


def serialize_func(obj, many):
    if many:
        return [
            ComplexP.model_validate(o).model_dump()
            for o in obj
        ]
    serializer = ComplexP.model_validate(obj)
    return serializer.model_dump()


def deserialize_func(obj, many):
    if many:
        return [ComplexPValidator(**o).build_dto() for o in obj]
    return ComplexPValidator(**obj).build_dto()
