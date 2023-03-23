import datetime
from dataclasses import dataclass
from typing import List, Optional

from player_stats.models.base_entity import BaseEntity


@dataclass(frozen=True)
class Player(BaseEntity):
    name: Optional[str]
    age: Optional[int]
    birth_date: Optional[str]
    height: Optional[int]
    place_of_birth: Optional[str]
    citenzenship: List[str]
    position: Optional[str]
    foot: Optional[str]
    agent: Optional[str]
    current_club: Optional[str]
    current_club_since: Optional[str]
    current_club_since: Optional[str]
    contract_until: Optional[str]
    last_contract_extension: Optional[str]
