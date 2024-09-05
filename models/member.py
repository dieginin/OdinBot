from enum import Enum

from helpers import from_int, from_str, to_class, to_enum

from .icon import Icon


class Role(Enum):
    MEMBER = "member"
    PRESIDENT = "president"
    SENIOR = "senior"
    VICE_PRESIDENT = "vicePresident"


class Member:
    def __init__(
        self,
        tag: str,
        name: str,
        name_color: str,
        role: Role,
        trophies: int,
        icon: Icon,
    ) -> None:
        self.tag = tag
        self.name = name
        self.name_color = name_color
        self.role = role
        self.trophies = trophies
        self.icon = icon

    @staticmethod
    def from_dict(obj: dict) -> "Member":
        tag = from_str(obj.get("tag"))
        name = from_str(obj.get("name"))
        name_color = from_str(obj.get("nameColor"))
        role = Role(obj.get("role"))
        trophies = from_int(obj.get("trophies"))
        icon = Icon.from_dict(obj.get("icon", {}))
        return Member(tag, name, name_color, role, trophies, icon)

    def to_dict(self) -> dict:
        result: dict = {}
        result["tag"] = from_str(self.tag)
        result["name"] = from_str(self.name)
        result["nameColor"] = from_str(self.name_color)
        result["role"] = to_enum(Role, self.role)
        result["trophies"] = from_int(self.trophies)
        result["icon"] = to_class(Icon, self.icon)
        return result
