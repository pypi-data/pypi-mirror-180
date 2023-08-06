from typing import Any


def get_nested(a: Any, key: str):
    res = a
    for k in key.split("."):
        res = getattr(res, k)
    return res
