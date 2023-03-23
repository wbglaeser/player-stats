import re
from typing import List, Optional

from player_stats.spiders.base_spider import BaseSpider
from player_stats.spiders.player_spider import PlayerSpider
from player_stats.models.player import Player
from player_stats.models.team import Team


class TeamSpider(BaseSpider):

    def __init__(self, url):
        super().__init__(url)

    def _name(self) -> str:
        return self.soup.find(
            "h1", {"class": "data-header__headline-wrapper data-header__headline-wrapper--oswald"}
        ).text

    def _players_links(self) -> List[str]:
        wrapped_links = self.soup.find("table", {"class": "items"}).find_all("td", {"class": "hauptlink"})
        stumped_links = filter(None, [x.find("span", {"class": "hide-for-small"}) for x in wrapped_links])
        return ["https://www.transfermarkt.de" + x.find("a")["href"] for x in stumped_links]

    def _players(self) -> List[Player | None]:
        players = []
        for link in self._players_links():
            players.append(PlayerSpider(link).scrape())
        return players

    def build_entity(self) -> Optional[Team]:
        name = self._name()
        players = self._players()
        return Team(
            name=name,
            players=players
        )
