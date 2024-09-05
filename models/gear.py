from helpers import from_int, from_str


class Gear:
    def __init__(self, id: int, name: str, level: int) -> None:
        self.id = id
        self.name = name
        self.level = level

    @staticmethod
    def from_dict(obj: dict) -> "Gear":
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        level = from_int(obj.get("level"))
        return Gear(id, name, level)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["level"] = from_int(self.level)
        return result
