import requests

from config import BS_KEY
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
    def get_club(self, tag: str) -> Club:
        url = CLUB_BASE_URL + parse_tag(tag)
        response = make_request(url)

        if response:
            return Club.from_dict(response)
        raise Exception("Tag no encontrada")

    def get_club_members(self, tag: str) -> list[Member]:
        url = CLUB_BASE_URL + parse_tag(tag) + "/members"
        response = make_request(url)

        if response:
            return [Member.from_dict(m) for m in response["items"]]
        raise Exception("Tag no encontrada")

    def get_player(self, tag: str) -> Player:
        url = PLYR_BASE_URL + parse_tag(tag)
        response = make_request(url)

        if response:
            return Player.from_dict(response)
        raise Exception("Tag no encontrada")

    def get_player_battlelog(self, tag: str) -> list[BattleLog]:
        url = PLYR_BASE_URL + parse_tag(tag) + "/battlelog"
        response = make_request(url)

        if response:
            return [BattleLog.from_dict(bl) for bl in response["items"]]
        raise Exception("Tag no encontrada")

    def get_brawlers(self) -> list[Brawler]:
        url = BWRS_BASE_URL
        response = make_request(url)

        if response:
            return [Brawler.from_dict(b) for b in response["items"]]
        raise Exception("Error en petición")

    def get_brawler_by_id(self, id: int) -> Brawler:
        url = BWRS_BASE_URL + str(id)
        response = make_request(url)

        if response:
            return Brawler.from_dict(response)
        raise Exception("ID no encontrada")
