import re
from typing import List

from player_stats.spiders.base_spider import BaseSpider
from player_stats.spiders.team_spider import TeamSpider
from player_stats.models.league import League
from player_stats.models.team import Team


class LeagueSpider(BaseSpider):

    def __init__(self, url):
        super().__init__(url)

    def _name(self) -> str:
        name = self.soup.find("h1", {"class": "data-header__headline-wrapper"}).text
        return re.sub(r"\n ", "", name).strip()

    def _team_links(self) -> List[str]:
        wrapped_links = self.soup.find(
            "table", {"class": "items"}
        ).find_all("td", {"class": "hauptlink no-border-links"})
        stumped_links = filter(None, [x.find("a")["href"] for x in wrapped_links])
        return ["https://www.transfermarkt.de" + x for x in stumped_links]

    def _teams(self) -> List[Team | None]:
        teams = []
        for link in self._team_links():
            team = TeamSpider(link).scrape()
            if team is not None:
                teams.append(team)
            else:
                print(f"Team not found at {link}")
        return teams

    def build_entity(self) -> League:
        name = self._name()
        teams = self._teams()
        self.entity = League(name=name, teams=teams)
        return self.entity
