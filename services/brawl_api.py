import requests

from config import BS_KEY
from helpers import from_list, to_response
from models import BattleLog, Brawler, Club, Member, Player

__BASE_URL = "https://bsproxy.royaleapi.dev/v1/"
CLUB_BASE_URL = __BASE_URL + "clubs/%23"
PLYR_BASE_URL = __BASE_URL + "players/%23"
BWRS_BASE_URL = __BASE_URL + "brawlers/"

parse_tag = lambda tag: tag.strip("#").strip().upper()


def make_request(url: str) -> dict | None:
    request = requests.get(url, headers={"Authorization": f"Bearer {BS_KEY}"})
    if request.status_code == 200:
        return request.json()


class BrawlApi:
    def get_club(self, tag: str) -> Club | None:
        url = CLUB_BASE_URL + parse_tag(tag)
        return to_response(Club, make_request(url))

    def get_club_members(self, tag: str) -> list[Member] | None:
        url = CLUB_BASE_URL + parse_tag(tag) + "/members"
        res = make_request(url)
        return from_list(Member.from_dict, res["items"]) if res else None

    def get_player(self, tag: str) -> Player | None:
        url = PLYR_BASE_URL + parse_tag(tag)
        return to_response(Player, make_request(url))

    def get_player_battlelog(self, tag: str) -> list[BattleLog] | None:
        url = PLYR_BASE_URL + parse_tag(tag) + "/battlelog"
        res = make_request(url)
        return from_list(BattleLog.from_dict, res["items"]) if res else None

    def get_brawlers(self) -> list[Brawler] | None:
        url = BWRS_BASE_URL
        res = make_request(url)
        return from_list(Brawler.from_dict, res["items"]) if res else None

    def get_brawler_by_id(self, id: int) -> Brawler | None:
        url = BWRS_BASE_URL + str(id)
        return to_response(Brawler, make_request(url))
