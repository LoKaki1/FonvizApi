from alpaca.trading import Position

from Common.Logger.Logger import logger_info_decorator
from Pullers.StocksDataPuller.IStocksDataPuller import IStocksDataPuller
from Trading.AccountManager.IAccountManager import IAccountManager
from Trading.Strategy.IStrategy import IStrategy


class CloserStrategy(IStrategy):

    def __init__(self,
                 account_manager: IAccountManager):
        self.account_manager = account_manager

    @logger_info_decorator
    def trade_strategy(self, ticker: str, **kwargs) -> dict[str, object]:
        return {
            'ticker': ticker,
            'type_of_order': 'sell',
            'qty': kwargs['qty']
        }

