from typing import NewType, TypeAlias, Iterable, Union, Optional, TYPE_CHECKING, List

if TYPE_CHECKING:
    from src.entity.resource.dto import ResourceDTO

__all__ = (
    'ResourceId',
    'ResourceOneOrList',
    'ResourceIdOneOrIterable'

)
ResourceId = NewType('ResourceId', int)

ResourceIdOneOrIterable: TypeAlias = Union[ResourceId, Iterable[ResourceId]]
ResourceOneOrList: TypeAlias = Union[Optional['ResourceDTO'] | List['ResourceDTO']]