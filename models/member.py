class Member:
    def __init__(self, tag: str, name: str, trophies: int) -> None:
        self.tag = tag
        self.name = name
        self.trophies = trophies

    def to_dict(self) -> dict:
        return {"tag": self.tag, "name": self.name, "trophies": self.trophies}

    @staticmethod
    def from_dict(obj: dict) -> "Member":
        tag = obj.get("tag") or ""
        name = obj.get("name") or ""
        trophies = obj.get("trophies") or 0
        return Member(tag, name, trophies)
