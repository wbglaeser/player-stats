from dataclasses import dataclass, asdict
from typing import List, Optional
import pandas as pd

from player_stats.models.player import Player
from player_stats.models.base_entity import BaseEntity


@dataclass(frozen=True)
class FielderMatchDay(BaseEntity):
    number: int
    date: str
    home_team: bool
    opponent: str
    result: str
    player_state: Optional[str] = "playing"
    position: Optional[str] = None
    goals: Optional[int] = None
    assists: Optional[int] = None
    yellow_card: Optional[int] = None
    yell_red_card: Optional[int] = None
    red_card: Optional[int] = None
    minutes_played: Optional[int] = None

    def _implement_pd_conversion(self) -> pd.DataFrame:
        pass
