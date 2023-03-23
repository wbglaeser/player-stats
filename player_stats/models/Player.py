import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class Player:
    name: str
    age: str
    birth_date: str
    height: str
    place_of_birth: str
    country_of_birth: str
    citenzenship: str
    position: str
    foot: str
    agent: str
    current_club: str
    current_club_since: str
    current_club_since: str
    contract_until: str
    last_contract_extension: str
