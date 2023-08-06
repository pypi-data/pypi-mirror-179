from abc import ABC
from typing import Type

from django.contrib.auth import get_user_model
from strawberry.types import Info

import gqlauth.core.field_
from gqlauth.core.utils import hide_args_kwargs, inject_arguments
from gqlauth.user.resolvers import BaseMixin

UserModel = get_user_model()


class ArgMixin(BaseMixin, ABC):
    def __init_subclass__(cls: Type[BaseMixin], **kwargs):
        input_type = cls.resolve_mutation.__annotations__["input_"]
        return_type = cls.resolve_mutation.__annotations__["return"]

        @gqlauth.core.field_.field(description=cls.__doc__, directives=cls.directives)
        @inject_arguments(input_type.__annotations__)
        @hide_args_kwargs
        def field(info: Info, **kwargs) -> return_type:  # type: ignore
            return cls.resolve_mutation(info, input_type(**kwargs))  # type: ignore

        cls.field = field  # type: ignore


class RelayMixin(BaseMixin, ABC):
    def __init_subclass__(cls: Type[BaseMixin], **kwargs):
        input_type = cls.resolve_mutation.__annotations__["input_"]
        return_type = cls.resolve_mutation.__annotations__["return"]

        @gqlauth.core.field_.field(description=cls.__doc__, directives=cls.directives)
        @hide_args_kwargs
        def field(info: Info, input: input_type) -> return_type:  # type: ignore
            return cls.resolve_mutation(info, input)  # type: ignore

        cls.field = field  # type: ignore
