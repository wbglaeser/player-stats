import re
from typing import Dict

from player_stats.spiders.base_spider import BaseSpider
from player_stats.models.Player import Player


class PlayerSpider(BaseSpider):

    def __init__(self, url):
        super().__init__(url)
        self.soup = self.cook_the_soup()

    def _name(self) -> str:
        name_raw = self.soup.find("h1", {"class": "data-header__headline-wrapper"}).text
        pattern = re.compile(r"[\n#0-9]")
        return re.sub(pattern, "", name_raw).strip()

    def _number(self) -> int:
        number_raw = self.soup.find("span", {"class": "data-header__shirt-number"}).text
        pattern = re.compile(r"[\n#]")
        return int(re.sub(pattern, "", number_raw).strip())

    def _player_base_stats(self) -> Dict[str, str]:
        stats_keys = [x.text for x in
                      self.soup.find_all("span", {"class": "info-table__content info-table__content--regular"})]
        stats_values = [x.text for x in
                        self.soup.find_all("span", {"class": "info-table__content info-table__content--bold"})]
        stats_dict = dict(zip(stats_keys, stats_values))

        base_state = {
            "birth_date": stats_dict["Geburtsdatum:"],
            "birth_place": stats_dict["Geburtsort:"],
            "age": stats_dict["Alter:"],
            "height": stats_dict["Größe:"],
            "nationality": stats_dict["Nationalität:"],
            "position": stats_dict["Position:"],
            "foot": stats_dict["Fuß:"]
        }
        return base_state

    def build_player(self) -> Player:
        base_stats = self._player_base_stats()
        return Player(
            name=self._name(),
            age=base_stats["age"],
            birth_date=base_stats["birth_date"],
            height=base_stats["height"],
            place_of_birth=base_stats["birth_place"],
            country_of_birth=base_stats["nationality"],
            citenzenship=base_stats["nationality"],
            position=base_stats["position"],
            foot=base_stats["foot"],
        )
