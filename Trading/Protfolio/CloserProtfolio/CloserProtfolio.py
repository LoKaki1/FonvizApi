from Trading.AccountManager.IAccountManager import IAccountManager
from Trading.Protfolio.CloserProtfolio.ICloserProtfolio import ICloserProtfolio
from Trading.TraderStrategy.ITraderStrategy import ITraderStrategy


class CloserProtfolio(ICloserProtfolio):
    def __init__(self,
                 closer_strategy_trader: ITraderStrategy,
                 account_manager: IAccountManager):
        self.account_manager = account_manager
        self.closer_strategy_trader = closer_strategy_trader

    def close_open_trades(self, **kwargs):
        account = self.account_manager.get_account()
        self.account_manager.close_all_positions()

        for trade in account.open_trades:
            self.closer_strategy_trader.trade_strategy(trade.symbol, quantity=trade.qty)
