from dataclasses import dataclass
from typing import Any


@dataclass
class AccountModel:
    money: float
    open_trades: Any
    open_positions: Any
