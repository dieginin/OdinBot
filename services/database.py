import pyrebase
import pyrebase.pyrebase as pb

from config import DB_CONFIG
from models import Club

from .brawl_api import BrawlApi

parse_tag = lambda tag: tag.strip("#").strip().upper()


class Database:
    def __init__(self) -> None:
        self.__db = pyrebase.initialize_app(DB_CONFIG).database()
        self.__ba = BrawlApi()

    @property
    def __clubs(self) -> pb.Database:
        return self.__db.child("clubs")

    def get_clubs(self) -> list[Club] | None:
        clubs = self.__clubs.get()
        if clubs.val():
            return [Club.from_dict(m.val()) for m in clubs]

    def set_club(self, tag: str) -> str:
        tag = parse_tag(tag)
        club = self.__ba.get_club(tag)
        if not club:
            return f"Ningun club con el tag #{tag} fue encontrado"

        clubs = self.__clubs.get()
        if clubs.val() and tag in [m.key() for m in clubs]:
            return f"El club {club.name} ya existe en la base de datos"

        self.__clubs.child(tag).set(club.to_dict())
        return f"{club.name} fue guardado en la base de datos exitosamente"

    def remove_club(self, tag: str) -> str:
        tag = parse_tag(tag)
        club = self.__ba.get_club(tag)
        if not club:
            return f"Ningun club con el tag #{tag} fue encontrado"
        self.__clubs.child(tag).remove()
        return f"{club.name} fue eliminado en la base de datos exitosamente"
