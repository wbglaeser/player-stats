import datetime
from dataclasses import dataclass, asdict
from typing import List, Optional
import pandas as pd

from player_stats.models.base_entity import BaseEntity


@dataclass(frozen=True)
class PlayerPerformance(BaseEntity):
    last_goal: Optional[str]

    def _implement_pd_conversion(self) -> pd.DataFrame:
        return pd.DataFrame([asdict(self)])
