from alpaca.trading import Position

from Common.Logger.Logger import logger_info_decorator, log_info
from Scanner.Abstracts.IScannerEverything import IScannerEverything
from Trading.AccountManager.IAccountManager import IAccountManager
from Trading.TraderManager.ITraderManager import ITraderManager
from Trading.TraderStrategy.ITraderStrategy import ITraderStrategy


class TraderManager(ITraderManager):

    def __init__(self,
                 scanner: IScannerEverything,
                 trader_strategy: ITraderStrategy,
                 closer_trader: ITraderStrategy,
                 account_manager: IAccountManager,

                 default_scanner_args: dict):
        self.closer_trader = closer_trader
        self.account_manager = account_manager
        self.default_scanner_args = default_scanner_args
        self.trader_strategy = trader_strategy
        self.scanner = scanner

    @logger_info_decorator
    def trade_according_to_scanner(self, **kwargs):
        self.close_trading()

        if kwargs is None or not len(kwargs):
            kwargs = self.default_scanner_args

        tickers = self.scanner.scan(**kwargs)

        log_info(tickers)

        for ticker in tickers:
            self.trader_strategy.trade_strategy(ticker)

    def close_trading(self):
        account = self.account_manager.get_account()

        for position in account.open_positions:
            self.closer_trader.trade_strategy(position.symbol, qty=position.qty)