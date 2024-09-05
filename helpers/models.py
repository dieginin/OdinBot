from enum import Enum
from typing import Any, Callable, Type, cast


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list[T](f: Callable[[Any], T], x: Any) -> list[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x) -> Any:
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class[T](c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum[EnumT: Enum](c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value
