from Common.Logger.Logger import logger_info_decorator
from Trading.OrdersSender.IOrderSender import IOrderSender
from Trading.Strategy.IStrategy import IStrategy
from Trading.TraderStrategy.ITraderStrategy import ITraderStrategy


class SmartTrader(ITraderStrategy):

    def __init__(self,
                 strategy: IStrategy,
                 order_sender: IOrderSender):
        self.order_sender = order_sender
        self.strategy = strategy

    @logger_info_decorator
    def trade_strategy(self, ticker: str, **kwargs):
        order_kwargs = self.strategy.trade_strategy(ticker, **kwargs)

        if 'price' in order_kwargs:
            self.order_sender.send_limit_order(**order_kwargs)

        else:
            self.order_sender.make_market_order(ticker, **order_kwargs)