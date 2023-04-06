import re
from typing import List
import pandas as pd
from dataclasses import asdict

from player_stats.spiders.base_spider import BaseSpider
from player_stats.models.player_performance import PlayerPerformance
from player_stats.models.fielder_match_day import FielderMatchDay


class PlayerPerformanceSpider(BaseSpider):

    def __init__(self, url):
        super().__init__(url)

    def _build_fielder_match_days(self) -> List[FielderMatchDay]:
        league_match_days = self.soup.find_all("div", {"class": "responsive-table"})[1].find("tbody").find_all("tr")
        fielder_match_days = []
        for match_day in league_match_days:
            match_days_stats = match_day.find_all("td")
            player_state = 0
            if len(match_day["class"]) > 0:
                match match_day["class"][0]:
                    case "bg_rot_20":
                        player_state = 1
                    case "bg_gelb_20":
                        player_state = 2
            if player_state != 0:
                fmd = FielderMatchDay(
                    name=re.sub(r"\n", r"", match_days_stats[0].text),
                    number=int(re.sub(r"\n", r"", match_days_stats[0].text)),
                    date=match_days_stats[1].text,
                    home_team=True if match_days_stats[2].text == "H" else False,
                    opponent=re.sub(r"[(\d{1,2}\.)]", r"", match_days_stats[6].text).replace(u'\xa0', u''),
                    result=match_days_stats[7].text.strip(),
                    player_state=match_days_stats[8].text
                )
            else:
                fmd = FielderMatchDay(
                    name=re.sub(r"\n", r"", match_days_stats[0].text),
                    number=int(re.sub(r"\n", r"", match_days_stats[0].text)),
                    date=match_days_stats[1].text,
                    home_team=True if match_days_stats[2].text == "H" else False,
                    opponent=re.sub(r"[(\d{1,2}\.)]", r"", match_days_stats[6].text).replace(u'\xa0', u''),
                    result=match_days_stats[7].text.strip(),
                    position=match_days_stats[8].text,
                    goals=match_days_stats[9].text,
                    assists=match_days_stats[10].text,
                    yellow_card=None if not match_days_stats[11].text.isnumeric() else int(
                        match_days_stats[11].text.strip("'")),
                    yell_red_card=None if not match_days_stats[12].text.isnumeric() else int(
                        match_days_stats[12].text.strip("'")),
                    red_card=None if not match_days_stats[13].text.isnumeric() else int(match_days_stats[13].text.strip("'")),
                    minutes_played=int(match_days_stats[14].text.strip("'"))
                )
            fielder_match_days.append(fmd)
        return fielder_match_days

    def build_entity(self) -> PlayerPerformance:
        fielder_match_days = self._build_fielder_match_days()
        return self.entity
