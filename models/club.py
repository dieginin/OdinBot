class Club:
    def __init__(self, tag: str, name: str) -> None:
        self.tag = tag
        self.name = name

    def to_dict(self) -> dict:
        return {"tag": self.tag, "name": self.name}

    @staticmethod
    def from_dict(obj: dict) -> "Club":
        tag = obj.get("tag") or ""
        name = obj.get("name") or ""
        return Club(tag, name)
