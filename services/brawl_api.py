import requests

from config import BS_KEY
from models import Club, Member

__BASE_URL = "https://bsproxy.royaleapi.dev/v1/"
CLUB_BASE_URL = __BASE_URL + "clubs/%23"

parse_tag = lambda tag: tag.strip("#").strip().upper()


def make_request(url: str) -> dict | None:
    request = requests.get(url, headers={"Authorization": f"Bearer {BS_KEY}"})
    if request.status_code == 200:
        return request.json()


class BrawlApi:
    def get_club(self, tag: str) -> Club | None:
        tag = parse_tag(tag)
        url = CLUB_BASE_URL + tag
        request = make_request(url)

        if request:
            return Club.from_dict(request)
        raise Exception(f"Tag #{tag} no encontrada")

    def get_club_members(self, tag: str) -> list[Member] | None:
        tag = parse_tag(tag)
        url = CLUB_BASE_URL + tag + "/members"
        request = make_request(url)

        if request:
            return [Member.from_dict(m) for m in request["items"]]
        raise Exception(f"Tag #{tag} no encontrada")
