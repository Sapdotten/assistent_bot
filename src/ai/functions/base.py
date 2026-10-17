from enum import Enum

from pydantic import BaseModel, model_validator
from typing_extensions import Self


class AiException(Exception):
    pass


class PropertyType(str, Enum):
    array = "array"
    string = "string"
    object = "object"


class BaseProperty(BaseModel):
    type: PropertyType


class StringProperty(BaseProperty):
    type: PropertyType = PropertyType.string
    description: str


class BaseParameters(BaseModel):
    type: PropertyType = PropertyType.object
    properties: dict[str, BaseProperty]
    required: list = []  # TODO: fix to factory later

    @model_validator(mode='after')
    def check_required(self) -> Self:
        for required in self.required:
            if required not in self.properties:
                raise AiException
        return self


class BaseFunction(BaseModel):
    type: str = 'function'
    name: str | None = None
    description: str | None = None
    parameters: BaseParameters
