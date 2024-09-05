from helpers import from_int


class Icon:
    def __init__(self, id: int) -> None:
        self.id = id

    @staticmethod
    def from_dict(obj: dict) -> "Icon":
        id = from_int(obj.get("id"))
        return Icon(id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        return result
