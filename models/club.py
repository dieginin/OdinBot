from helpers import from_int, from_str


class Club:
    def __init__(
        self, tag: str, name: str, description: str, badge_id: int, trophies: int
    ) -> None:
        self.tag = tag
        self.name = name
        self.description = description
        self.badge_id = badge_id
        self.trophies = trophies

    @staticmethod
    def from_dict(obj: dict) -> "Club":
        tag = from_str(obj.get("tag"))
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        badge_id = from_int(obj.get("badgeId"))
        trophies = from_int(obj.get("trophies"))
        return Club(tag, name, description, badge_id, trophies)

    def to_dict(self) -> dict:
        result: dict = {}
        result["tag"] = from_str(self.tag)
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["badgeId"] = from_int(self.badge_id)
        result["trophies"] = from_int(self.trophies)
        return result
