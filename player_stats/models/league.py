from dataclasses import dataclass
from typing import List
import pandas as pd

from player_stats.models.team import Team
from player_stats.models.base_entity import BaseEntity


@dataclass(frozen=True)
class League(BaseEntity):
    teams: List[Team]

    def _implement_pd_conversion(self) -> pd.DataFrame:
        df = pd.concat(team.convert_to_pd() for team in self.teams)
        df["league"] = self.name
        return df
