from dataclasses import dataclass, asdict
from typing import List
import pandas as pd

from player_stats.models.player import Player
from player_stats.models.base_entity import BaseEntity


@dataclass(frozen=True)
class Team(BaseEntity):
    players: List[Player]

    def _implement_pd_conversion(self) -> pd.DataFrame:
        df = pd.DataFrame([asdict(player) for player in self.players])
        df["team"] = self.name
        return df
