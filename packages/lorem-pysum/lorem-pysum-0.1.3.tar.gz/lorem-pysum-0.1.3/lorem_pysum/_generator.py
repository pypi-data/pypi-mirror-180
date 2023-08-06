"""Generate random instances of the given Pydantic model type."""
import random
import re
from enum import Enum
from typing import Any, Type, TypeVar
from uuid import UUID, uuid4

from pydantic import BaseModel
from pydantic.fields import ModelField

ModelType = TypeVar("ModelType", bound=BaseModel)
# noinspection SpellCheckingInspection
lorem = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
"""


def generate(
    model_type: Type[ModelType],
    use_default_values: bool = True,
    optionals_use_none: bool = False,
    **kwargs: Any,
) -> ModelType:
    """Generate an instance of a Pydantic model with random values.

    Any values provided in `kwargs` will be used as model field values
    instead of randomly generating them.

    :param model_type: Model type to generate an instance of.
    :param use_default_values: Whether to use model default values.
    :param optionals_use_none: How to handle optional fields.
    :param kwargs: Attributes to set on the model instance.
    :return: A randomly generated instance of the provided model type.
    """
    for field_name, model_field in model_type.__fields__.items():
        if field_name in kwargs:
            continue
        if model_field.default is not None or model_field.default_factory is not None:
            if use_default_values:
                continue

        kwargs[field_name] = _get_value(
            model_field, use_default_values, optionals_use_none
        )
    return model_type(**kwargs)


def _get_value(
    model_field: ModelField, use_default_values: bool, optionals_use_none: bool
) -> Any:
    if model_field.allow_none and optionals_use_none:
        return None
    if model_field.type_ == str:
        return random_str()
    if model_field.type_ == int:
        return random.randint(0, 100)
    if model_field.type_ == float:
        return random.random() * 100
    if model_field.type_ == bool:
        return random.random() > 0.5
    if issubclass(model_field.type_, BaseModel):
        return generate(model_field.type_, use_default_values, optionals_use_none)
    if issubclass(model_field.type_, Enum):
        return random.choices(list(model_field.type_))[0]
    if model_field.type_ == UUID:
        return uuid4()


def random_str() -> str:
    """Get a random string."""
    return random.choices(re.findall(r"(\S+)", lorem))[0]
