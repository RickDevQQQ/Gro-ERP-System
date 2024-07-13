from typing import Optional

from fastapi import HTTPException

__all__ = (
    'ValidationResult',
)


class ValidationResult:

    def __init__(
        self,
        is_valid: bool,
        detail: Optional[str] = None,
        data: Optional[dict] = None,
        status_code: Optional[int] = None,
    ) -> None:
        self.is_valid = is_valid
        self.detail = detail
        self.data = data
        self.status_code = status_code

    def raise_for_is_valid(self) -> None:
        if self.is_valid:
            return
        raise HTTPException(status_code=self.status_code, detail={
            'message': self.detail,
            'data': self.data
        })

    def __bool__(self) -> bool:
        return self.is_valid
