from dataclasses import dataclass


@dataclass
class AccountModel:
    money: float
    open_trades: int
