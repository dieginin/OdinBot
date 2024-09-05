from helpers import from_bool, from_int, from_list, from_str, to_class

from .gadget import Gadget
from .gear import Gear
from .icon import Icon


class Brawler:
    def __init__(
        self,
        id: int,
        name: str,
        power: int,
        rank: int,
        trophies: int,
        highest_trophies: int,
        gears: list[Gear],
        star_powers: list[Gadget],
        gadgets: list[Gadget],
    ) -> None:
        self.id = id
        self.name = name
        self.power = power
        self.rank = rank
        self.trophies = trophies
        self.highest_trophies = highest_trophies
        self.gears = gears
        self.star_powers = star_powers
        self.gadgets = gadgets

    @staticmethod
    def from_dict(obj: dict) -> "Brawler":
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        power = from_int(obj.get("power"))
        rank = from_int(obj.get("rank"))
        trophies = from_int(obj.get("trophies"))
        highest_trophies = from_int(obj.get("highestTrophies"))
        gears = from_list(Gear.from_dict, obj.get("gears"))
        star_powers = from_list(Gadget.from_dict, obj.get("starPowers"))
        gadgets = from_list(Gadget.from_dict, obj.get("gadgets"))
        return Brawler(
            id,
            name,
            power,
            rank,
            trophies,
            highest_trophies,
            gears,
            star_powers,
            gadgets,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["power"] = from_int(self.power)
        result["rank"] = from_int(self.rank)
        result["trophies"] = from_int(self.trophies)
        result["highestTrophies"] = from_int(self.highest_trophies)
        result["gears"] = from_list(lambda x: to_class(Gear, x), self.gears)
        result["starPowers"] = from_list(
            lambda x: to_class(Gadget, x), self.star_powers
        )
        result["gadgets"] = from_list(lambda x: to_class(Gadget, x), self.gadgets)
        return result


class Club:
    def __init__(self, tag: str, name: str) -> None:
        self.tag = tag
        self.name = name

    @staticmethod
    def from_dict(obj: dict) -> "Club":
        tag = from_str(obj.get("tag"))
        name = from_str(obj.get("name"))
        return Club(tag, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["tag"] = from_str(self.tag)
        result["name"] = from_str(self.name)
        return result


class Player:
    def __init__(
        self,
        tag: str,
        name: str,
        name_color: str,
        icon: Icon,
        trophies: int,
        highest_trophies: int,
        exp_level: int,
        exp_points: int,
        is_qualified_from_championship_challenge: bool,
        the_3_vs3_victories: int,
        solo_victories: int,
        duo_victories: int,
        best_robo_rumble_time: int,
        best_time_as_big_brawler: int,
        club: Club,
        brawlers: list[Brawler],
    ) -> None:
        self.tag = tag
        self.name = name
        self.name_color = name_color
        self.icon = icon
        self.trophies = trophies
        self.highest_trophies = highest_trophies
        self.exp_level = exp_level
        self.exp_points = exp_points
        self.is_qualified_from_championship_challenge = (
            is_qualified_from_championship_challenge
        )
        self.the_3_vs3_victories = the_3_vs3_victories
        self.solo_victories = solo_victories
        self.duo_victories = duo_victories
        self.best_robo_rumble_time = best_robo_rumble_time
        self.best_time_as_big_brawler = best_time_as_big_brawler
        self.club = club
        self.brawlers = brawlers

    @staticmethod
    def from_dict(obj: dict) -> "Player":
        tag = from_str(obj.get("tag"))
        name = from_str(obj.get("name"))
        name_color = from_str(obj.get("nameColor"))
        icon = Icon.from_dict(obj.get("icon", {}))
        trophies = from_int(obj.get("trophies"))
        highest_trophies = from_int(obj.get("highestTrophies"))
        exp_level = from_int(obj.get("expLevel"))
        exp_points = from_int(obj.get("expPoints"))
        is_qualified_from_championship_challenge = from_bool(
            obj.get("isQualifiedFromChampionshipChallenge")
        )
        the_3_vs3_victories = from_int(obj.get("3vs3Victories"))
        solo_victories = from_int(obj.get("soloVictories"))
        duo_victories = from_int(obj.get("duoVictories"))
        best_robo_rumble_time = from_int(obj.get("bestRoboRumbleTime"))
        best_time_as_big_brawler = from_int(obj.get("bestTimeAsBigBrawler"))
        club = Club.from_dict(obj.get("club", {}))
        brawlers = from_list(Brawler.from_dict, obj.get("brawlers"))
        return Player(
            tag,
            name,
            name_color,
            icon,
            trophies,
            highest_trophies,
            exp_level,
            exp_points,
            is_qualified_from_championship_challenge,
            the_3_vs3_victories,
            solo_victories,
            duo_victories,
            best_robo_rumble_time,
            best_time_as_big_brawler,
            club,
            brawlers,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["tag"] = from_str(self.tag)
        result["name"] = from_str(self.name)
        result["nameColor"] = from_str(self.name_color)
        result["icon"] = to_class(Icon, self.icon)
        result["trophies"] = from_int(self.trophies)
        result["highestTrophies"] = from_int(self.highest_trophies)
        result["expLevel"] = from_int(self.exp_level)
        result["expPoints"] = from_int(self.exp_points)
        result["isQualifiedFromChampionshipChallenge"] = from_bool(
            self.is_qualified_from_championship_challenge
        )
        result["3vs3Victories"] = from_int(self.the_3_vs3_victories)
        result["soloVictories"] = from_int(self.solo_victories)
        result["duoVictories"] = from_int(self.duo_victories)
        result["bestRoboRumbleTime"] = from_int(self.best_robo_rumble_time)
        result["bestTimeAsBigBrawler"] = from_int(self.best_time_as_big_brawler)
        result["club"] = to_class(Club, self.club)
        result["brawlers"] = from_list(lambda x: to_class(Brawler, x), self.brawlers)
        return result
