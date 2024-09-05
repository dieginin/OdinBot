from helpers import from_int, from_str


class Gadget:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    @staticmethod
    def from_dict(obj: dict) -> "Gadget":
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        return Gadget(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        return result
