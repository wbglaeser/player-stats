import re
from typing import Dict
import pandas as pd
from dataclasses import asdict

from player_stats.spiders.base_spider import BaseSpider
from player_stats.models.player import Player


class PlayerSpider(BaseSpider):

    def __init__(self, url):
        super().__init__(url)

    def _name(self) -> str:
        name_raw = self.soup.find("h1", {"class": "data-header__headline-wrapper"}).text
        pattern = re.compile(r"[\n#0-9]")
        return re.sub(pattern, "", name_raw).strip()

    def _number(self) -> int:
        number_raw = self.soup.find("span", {"class": "data-header__shirt-number"}).text
        pattern = re.compile(r"[\n#]")
        return int(re.sub(pattern, "", number_raw).strip())

    def _player_base_stats(self) -> Dict[str, str]:
        stats_keys = [re.sub(r"[\n:]", "", x.text).strip() for x in
                      self.soup.find_all("span", {"class": "info-table__content info-table__content--regular"})]
        stats_values = [re.sub(r"[\n:]", "", x.text).strip() for x in
                        self.soup.find_all("span", {"class": [
                            "info-table__content info-table__content--bold",
                            "info-table__content info-table__content--bold info-table__content--flex"
                        ]})]
        stats_dict = dict(zip(stats_keys, stats_values))

        base_state = {
            "birth_date": re.sub(r"Happy Birthday", "", stats_dict.get("Geburtsdatum", None)),
            "birth_place": stats_dict.get("Geburtsort", None),
            "age": int(stats_dict.get("Alter", None)),
            "height": int(re.sub(r"[,m]", "", stats_dict.get("Größe", None).replace(u'\xa0', u' '))),
            "nationality": re.sub(r" +", r" ", stats_dict.get("Nationalität", None).replace(u'\xa0', u' ')).split(" "),
            "position": stats_dict.get("Position", None),
            "foot": stats_dict.get("Fuß", None),
            "agent": stats_dict.get("Spielerberater", None),
            "current_club": stats_dict.get("Aktueller Verein", None),
            "current_club_since": stats_dict.get("Im Team seit", None),
            "contract_until": stats_dict.get("Vertrag bis", None),
            "last_contract_extension": stats_dict.get("Letzte Verlängerung", None)
        }
        return base_state

    def build_entity(self) -> Player:
        name = self._name()
        print("Scraping player: " + name)
        base_stats = self._player_base_stats()
        self.entity = Player(
            name=name,
            age=base_stats["age"],
            birth_date=base_stats["birth_date"],
            height=base_stats["height"],
            place_of_birth=base_stats["birth_place"],
            citizenship=base_stats["nationality"],
            position=base_stats["position"],
            foot=base_stats["foot"],
            agent=base_stats["agent"],
            current_club=base_stats["current_club"],
            current_club_since=base_stats["current_club_since"],
            contract_until=base_stats["contract_until"],
            last_contract_extension=base_stats["last_contract_extension"]
        )
        return self.entity
