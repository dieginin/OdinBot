from typing import Optional

from helpers import from_int, from_list, from_none, from_str, from_union, to_class


class Brawler:
    def __init__(
        self,
        id: int,
        name: str,
        power: int,
        trophies: int,
        trophy_change: Optional[int],
    ) -> None:
        self.id = id
        self.name = name
        self.power = power
        self.trophies = trophies
        self.trophy_change = trophy_change

    @staticmethod
    def from_dict(obj: dict) -> "Brawler":
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        power = from_int(obj.get("power"))
        trophies = from_int(obj.get("trophies"))
        trophy_change = from_union([from_int, from_none], obj.get("trophyChange"))
        return Brawler(id, name, power, trophies, trophy_change)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["power"] = from_int(self.power)
        result["trophies"] = from_int(self.trophies)
        if self.trophy_change is not None:
            result["trophyChange"] = from_union(
                [from_int, from_none], self.trophy_change
            )
        return result


class Player:
    def __init__(
        self,
        tag: str,
        name: str,
        brawlers: Optional[list[Brawler]],
        brawler: Optional[Brawler],
    ) -> None:
        self.tag = tag
        self.name = name
        self.brawlers = brawlers
        self.brawler = brawler

    @staticmethod
    def from_dict(obj: dict) -> "Player":
        tag = from_str(obj.get("tag"))
        name = from_str(obj.get("name"))
        brawlers = from_union(
            [lambda x: from_list(Brawler.from_dict, x), from_none], obj.get("brawlers")
        )
        brawler = from_union([Brawler.from_dict, from_none], obj.get("brawler"))
        return Player(tag, name, brawlers, brawler)

    def to_dict(self) -> dict:
        result: dict = {}
        result["tag"] = from_str(self.tag)
        result["name"] = from_str(self.name)
        if self.brawlers is not None:
            result["brawlers"] = from_union(
                [lambda x: from_list(lambda x: to_class(Brawler, x), x), from_none],
                self.brawlers,
            )
        if self.brawler is not None:
            result["brawler"] = from_union(
                [lambda x: to_class(Brawler, x), from_none], self.brawler
            )
        return result


class Battle:
    def __init__(
        self,
        mode: str,
        type: str,
        result: Optional[str],
        duration: Optional[int],
        trophy_change: Optional[int],
        star_player: Optional[Player],
        teams: Optional[list[list[Player]]],
        players: Optional[list[Player]],
        rank: Optional[int],
    ) -> None:
        self.mode = mode
        self.type = type
        self.result = result
        self.duration = duration
        self.trophy_change = trophy_change
        self.star_player = star_player
        self.teams = teams
        self.players = players
        self.rank = rank

    @staticmethod
    def from_dict(obj: dict) -> "Battle":
        mode = from_str(obj.get("mode"))
        type = from_str(obj.get("type"))
        result = from_union([from_str, from_none], obj.get("result"))
        duration = from_union([from_int, from_none], obj.get("duration"))
        trophy_change = from_union([from_int, from_none], obj.get("trophyChange"))
        star_player = from_union([Player.from_dict, from_none], obj.get("starPlayer"))
        teams = from_union(
            [
                lambda x: from_list(lambda x: from_list(Player.from_dict, x), x),
                from_none,
            ],
            obj.get("teams"),
        )
        players = from_union(
            [lambda x: from_list(Player.from_dict, x), from_none],
            obj.get("players"),
        )
        rank = from_union([from_int, from_none], obj.get("rank"))
        return Battle(
            mode,
            type,
            result,
            duration,
            trophy_change,
            star_player,
            teams,
            players,
            rank,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["mode"] = from_str(self.mode)
        result["type"] = from_str(self.type)
        if self.result is not None:
            result["result"] = from_union(
                [lambda x: from_str(x), from_none], self.result
            )
        if self.duration is not None:
            result["duration"] = from_union([from_int, from_none], self.duration)
        if self.trophy_change is not None:
            result["trophyChange"] = from_union(
                [from_int, from_none], self.trophy_change
            )
        if self.star_player is not None:
            result["starPlayer"] = from_union(
                [lambda x: to_class(Player, x), from_none], self.star_player
            )
        if self.teams is not None:
            result["teams"] = from_union(
                [
                    lambda x: from_list(
                        lambda x: from_list(lambda x: to_class(Player, x), x), x
                    ),
                    from_none,
                ],
                self.teams,
            )
        if self.players is not None:
            result["players"] = from_union(
                [lambda x: from_list(lambda x: to_class(Player, x), x), from_none],
                self.players,
            )
        if self.rank is not None:
            result["rank"] = from_union([from_int, from_none], self.rank)
        return result


class Event:
    def __init__(self, id: int, mode: Optional[str], map: Optional[str]) -> None:
        self.id = id
        self.mode = mode
        self.map = map

    @staticmethod
    def from_dict(obj: dict) -> "Event":
        id = from_int(obj.get("id"))
        mode = from_union([from_str, from_none], obj.get("mode"))
        map = from_union([from_str, from_none], obj.get("map"))
        return Event(id, mode, map)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        if self.mode is not None:
            result["mode"] = from_union([lambda x: from_str(x), from_none], self.mode)
        result["map"] = from_union([lambda x: from_str(x), from_none], self.map)
        return result


class BattleLog:
    def __init__(self, battle_time: str, event: Event, battle: Battle) -> None:
        self.battle_time = battle_time
        self.event = event
        self.battle = battle

    @staticmethod
    def from_dict(obj: dict) -> "BattleLog":
        battle_time = from_str(obj.get("battleTime"))
        event = Event.from_dict(obj.get("event", {}))
        battle = Battle.from_dict(obj.get("battle", {}))
        return BattleLog(battle_time, event, battle)

    def to_dict(self) -> dict:
        result: dict = {}
        result["battleTime"] = from_str(self.battle_time)
        result["event"] = to_class(Event, self.event)
        result["battle"] = to_class(Battle, self.battle)
        return result
