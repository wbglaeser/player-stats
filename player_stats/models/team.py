from dataclasses import dataclass
from typing import List
import pandas as pd

from player_stats.models.player import Player
from player_stats.models.base_entity import BaseEntity


@dataclass(frozen=True)
class Team(BaseEntity):
    name: str
    players: List[Player]
