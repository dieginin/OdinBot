from helpers import from_int, from_list, from_str, to_class

from .member import Member


class Club:
    def __init__(
        self,
        tag: str,
        name: str,
        description: str,
        type: str,
        badge_id: int,
        required_trophies: int,
        trophies: int,
        members: list[Member],
    ) -> None:
        self.tag = tag
        self.name = name
        self.description = description
        self.type = type
        self.badge_id = badge_id
        self.required_trophies = required_trophies
        self.trophies = trophies
        self.members = members

    @staticmethod
    def from_dict(obj: dict) -> "Club":
        tag = from_str(obj.get("tag"))
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        type = from_str(obj.get("type"))
        badge_id = from_int(obj.get("badgeId"))
        required_trophies = from_int(obj.get("requiredTrophies"))
        trophies = from_int(obj.get("trophies"))
        members = from_list(Member.from_dict, obj.get("members"))
        return Club(
            tag, name, description, type, badge_id, required_trophies, trophies, members
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["tag"] = from_str(self.tag)
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["type"] = from_str(self.type)
        result["badgeId"] = from_int(self.badge_id)
        result["requiredTrophies"] = from_int(self.required_trophies)
        result["trophies"] = from_int(self.trophies)
        result["members"] = from_list(lambda x: to_class(Member, x), self.members)
        return result
