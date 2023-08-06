from typing import Any, Hashable

from kumo.types import IndexSpec
from kumo.utils import get_nested


def get_index_value(data: Any, index_spec: IndexSpec) -> Hashable:
    if isinstance(index_spec, str):
        return get_nested(data, index_spec)
    return tuple(get_nested(data, s) for s in index_spec)