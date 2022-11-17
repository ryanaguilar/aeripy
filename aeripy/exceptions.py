"""aeripy exception classes.
Includes three main exceptions: :class:`.AeriesAPIException` for when something goes wrong
on the server side, and :class:`.ClientException` when something goes wrong on the
client side. These two classes extend :class:`.AeripyException`. A third class of exceptions
extend the pydantic base exception.
"""

from pydantic import ValidationError, PydanticValueError


class AeripyException(Exception):
    """The base aeripy Exception that all other exception classes extend"""
    pass


class StateEducatorIdError(ValidationError):
    """The StateEducatorId is longer than 10 digits"""
    pass
