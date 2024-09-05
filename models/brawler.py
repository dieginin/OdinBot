from helpers import from_int, from_list, from_str, to_class
from models.gadget import Gadget


class Brawler:
    def __init__(
        self, id: int, name: str, star_powers: list[Gadget], gadgets: list[Gadget]
    ) -> None:
        self.id = id
        self.name = name
        self.star_powers = star_powers
        self.gadgets = gadgets

    @staticmethod
    def from_dict(obj: dict) -> "Brawler":
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        star_powers = from_list(Gadget.from_dict, obj.get("starPowers"))
        gadgets = from_list(Gadget.from_dict, obj.get("gadgets"))
        return Brawler(id, name, star_powers, gadgets)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["starPowers"] = from_list(
            lambda x: to_class(Gadget, x), self.star_powers
        )
        result["gadgets"] = from_list(lambda x: to_class(Gadget, x), self.gadgets)
        return result
