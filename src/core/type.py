from typing import TypeAlias, Union

from sqlalchemy import BinaryExpression

FilterType: TypeAlias = Union[bool, BinaryExpression]