from math import ceil
from typing import Optional, Dict

from src.core.validation import ValidationResult
from fastapi import Query


class Paginator:

    def __init__(
        self,
        limit: int = 10,
        page: int = 1,
        filters: Optional[Dict] = None
    ) -> None:
        self.limit = limit
        self.page = page
        self.offset = (page - 1) * limit
        self.filters = filters or {}
        self.validate()

    def validate(self):
        if self.limit <= 0:
            return ValidationResult(
                is_valid=False, detail="Указан не корректный лимит на странице.", data={'value': self.limit}
            )
        if self.page <= 0:
            return ValidationResult(
                is_valid=False, detail="Указана не корректная страница.", data={'value': self.limit}
            )
        return ValidationResult(is_valid=True)

    def get_max_page(self, all_count: int) -> int:
        return ceil(all_count / self.limit)


def get_paginator_info(
    limit: int = Query(default=10, title="Максимальное количество элементов на странице"),
    page: int = Query(default=1, title="Номер страницы")
):
    return limit, page
