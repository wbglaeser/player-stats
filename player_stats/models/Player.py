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
    # current_club: str
    # joined_current_club: datetime.date
    # contract_expires: datetime.date
    # market_value: int

