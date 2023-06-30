from Common.Logger.Logger import logger_info_decorator
from Scanner.Abstracts.IScannerEverything import IScannerEverything
from Trading.TraderManager.ITraderManager import ITraderManager
from Trading.TraderStrategy.ITraderStrategy import ITraderStrategy


class TraderManager(ITraderManager):

    def __init__(self,
                 scanner: IScannerEverything,
                 trader_strategy: ITraderStrategy,
                 default_scanner_args: dict):
        self.default_scanner_args = default_scanner_args
        self.trader_strategy = trader_strategy
        self.scanner = scanner

    @logger_info_decorator
    def trade_according_to_scanner(self, **kwargs):
        if kwargs is None or not len(kwargs):
            kwargs = self.default_scanner_args

        tickers = self.scanner.scan(**kwargs)

        for ticker in tickers:
            self.trader_strategy.trade_strategy(ticker)

