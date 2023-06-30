from Common.Logger.Logger import logger_info_decorator
from Pullers.StocksDataPuller.IStocksDataPuller import IStocksDataPuller
from Trading.Strategy.IStrategy import IStrategy


class BasicStrategy(IStrategy):

    def __init__(self, data_puller: IStocksDataPuller):
        self.data_puller = data_puller
        self.money = 1000
        # should replace it with object that contains user data like money and alpaca classes will
        # also be able to edit it
        self.risk = 0.10
        self.profit = 0.10

    @logger_info_decorator
    def trade_strategy(self, ticker: str) -> dict[str, object]:
        close_price = self.data_puller.get_price(ticker, 'close', -1, interval='1m', _range='1d')
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
            'quantity': self.calculate_quantity(close_price),
            'price': close_price,
            'stop_loss': close_price - close_price * self.risk,
            'take_profit': close_price + close_price * self.profit
        }

    @logger_info_decorator
    def calculate_quantity(self, last_price: float) -> float:
        return (self.money / 10) // last_price
