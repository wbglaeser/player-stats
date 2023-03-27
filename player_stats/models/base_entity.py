from dataclasses import dataclass
import pandas as pd


@dataclass(frozen=True)
class BaseEntity:
    name: str

    def convert_to_pd(self) -> pd.DataFrame:
        if self is None:
            raise ValueError("Entity is None. Please build first.")
        return self._implement_pd_conversion()

    def _implement_pd_conversion(self) -> pd.DataFrame:
        raise NotImplementedError("Please implement this method in the subclass.")
