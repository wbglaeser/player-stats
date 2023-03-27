import datetime
from dataclasses import dataclass, asdict
from typing import List, Optional
import pandas as pd

from player_stats.models.base_entity import BaseEntity


@dataclass(frozen=True)
class Player(BaseEntity):
    age: Optional[str]
    birth_date: Optional[str]
    height: Optional[str]
    place_of_birth: Optional[str]
    citizenship: List[str]
    position: Optional[str]
    foot: Optional[str]
    agent: Optional[str]
    current_club: Optional[str]
    current_club_since: Optional[str]
    current_club_since: Optional[str]
    contract_until: Optional[str]
    last_contract_extension: Optional[str]

    def _implement_pd_conversion(self) -> pd.DataFrame:
        return pd.DataFrame([asdict(self)])
