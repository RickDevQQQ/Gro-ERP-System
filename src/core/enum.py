from enum import Enum


class SaveMethod(Enum):
    none = 0
    flush = 1
    commit = 2
