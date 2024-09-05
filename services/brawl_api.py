import requests

from config import BS_KEY
from models import Club, Member, Player

__BASE_URL = "https://bsproxy.royaleapi.dev/v1/"
CLUB_BASE_URL = __BASE_URL + "clubs/%23"
PLYR_BASE_URL = __BASE_URL + "players/%23"

parse_tag = lambda tag: tag.strip("#").strip().upper()


def make_request(url: str) -> dict | None:
    request = requests.get(url, headers={"Authorization": f"Bearer {BS_KEY}"})
    if request.status_code == 200:
        return request.json()


class BrawlApi:
    def get_club(self, tag: str) -> Club:
        tag = parse_tag(tag)
        url = CLUB_BASE_URL + tag
        response = make_request(url)

        if response:
            return Club.from_dict(response)
        raise Exception(f"Tag #{tag} no encontrada")

    def get_club_members(self, tag: str) -> list[Member]:
        tag = parse_tag(tag)
        url = CLUB_BASE_URL + tag + "/members"
        response = make_request(url)

        if response:
            return [Member.from_dict(m) for m in response["items"]]
        raise Exception(f"Tag #{tag} no encontrada")

    def get_player(self, tag: str) -> Player:
        tag = parse_tag(tag)
        url = PLYR_BASE_URL + tag
        response = make_request(url)

        if response:
            return Player.from_dict(response)
        raise Exception(f"Tag #{tag} no encontrada")
