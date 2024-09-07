from helpers import from_int, from_str, to_class

from .icon import Icon


class Member:
    def __init__(
        self,
        tag: str,
        name: str,
        club_tag: str,
        role: str,
        trophies: int,
        icon: Icon,
    ) -> None:
        self.tag = tag
        self.name = name
        self.role = role
        self.trophies = trophies
        self.icon = icon
        self.club_tag = club_tag

    @staticmethod
    def from_dict(obj: dict) -> "Member":
        tag = from_str(obj.get("tag"))
        name = from_str(obj.get("name"))
        club_tag = from_str(obj.get("club_tag"))
        role = from_str(obj.get("role"))
        trophies = from_int(obj.get("trophies"))
        icon = Icon.from_dict(obj.get("icon", {}))
        return Member(tag, name, club_tag, role, trophies, icon)

    def to_dict(self) -> dict:
        result: dict = {}
        result["tag"] = from_str(self.tag)
        result["name"] = from_str(self.name)
        result["club_tag"] = from_str(self.club_tag)
        result["role"] = from_str(self.role)
        result["trophies"] = from_int(self.trophies)
        result["icon"] = to_class(Icon, self.icon)
        return result
