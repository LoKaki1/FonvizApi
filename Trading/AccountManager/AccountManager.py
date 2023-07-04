from alpaca.trading import TradingClient

from Common.Models.AccountModel import AccountModel
from Trading.AccountManager.IAccountManager import IAccountManager


class AccountManager(IAccountManager):

    def __init__(self, trading_client: TradingClient):
        self.trading_client = trading_client
        self.account_model = AccountModel(0, 0, 0)

        self.update_acount()

    def update_acount(self):
        account = self.trading_client.get_account()
        self.account_model.money = round(float(account.cash), 2)
        self.account_model.open_trades = self.trading_client.get_orders()
        self.account_model.open_positions = self.trading_client.get_all_positions()

    def get_account(self) -> AccountModel:
        self.update_acount()

        return self.account_model

    def close_all_positions(self):
        self.trading_client.close_all_positions(True)
