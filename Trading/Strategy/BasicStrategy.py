from Common.Logger.Logger import logger_info_decorator
from Common.Models.AccountModel import AccountModel
from Pullers.StocksDataPuller.IStocksDataPuller import IStocksDataPuller
from Trading.AccountManager.IAccountManager import IAccountManager
from Trading.Strategy.IStrategy import IStrategy


class BasicStrategy(IStrategy):

    def __init__(self, data_puller: IStocksDataPuller, account_manager: IAccountManager):
        self.account_manager = account_manager
        self.data_puller = data_puller
        # should replace it with object that contains user data like money and alpaca classes will
        # also be able to edit it
        self.risk = 0.10
        self.profit = 0.10

    @logger_info_decorator
    def trade_strategy(self, ticker: str, **kwargs) -> dict[str, object]:
        close_price = self.data_puller.get_price(ticker, 'close', -1, interval='1m', _range='1d', **kwargs)
        """
            ticker: str,
            type_of_order: str,
            quantity: int,
            price: float,
            stop_loss: float,
            take_profit: float
        """
        return {
            'ticker': ticker,
            'type_of_order': 'buy',
            'quantity': round(self.calculate_quantity(close_price), 2),
            'price': round(close_price, 2),
            'stop_loss': round(close_price - close_price * self.risk, 2),
            'take_profit': round(close_price + close_price * self.profit, 2)
        }

    @logger_info_decorator
    def calculate_quantity(self, last_price: float) -> float:
        return (self.account_manager.get_account().money / 10) // last_price
