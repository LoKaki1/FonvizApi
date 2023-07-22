from Common.Logger.Logger import logger_info_decorator
from Common.TradingCommon import is_trading_time
from Pullers.StocksDataPuller.IStocksDataPuller import IStocksDataPuller
from Trading.AccountManager.IAccountManager import IAccountManager
from Trading.Strategy.IStrategy import IStrategy


class CloserStrategy(IStrategy):

    def __init__(self,
                 account_manager: IAccountManager,
                 stock_data_puller: IStocksDataPuller):
        self.stocks_data_puller = stock_data_puller
        self.account_manager = account_manager

    @logger_info_decorator
    def trade_strategy(self, ticker: str, **kwargs) -> dict[str, object]:
        base_close = {
            'ticker': ticker,
            'type_of_order': 'sell',
            'quantity': kwargs['quantity']
        }

        if not is_trading_time():
            last_price = self.stocks_data_puller.get_price(ticker, 'close', -1, interval='1m', _range='1d')
            base_close['price'] = last_price

        return base_close
