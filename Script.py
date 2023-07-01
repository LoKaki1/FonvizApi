import time
from datetime import datetime

from alpaca.trading import TradingClient

from Config.ConfigurationLoader import load_configuration
from Pullers.StocksDataPuller.YahooDataPuller import YahooDataPuller
from Scanner.FinvizScanner import FinvizScanner
from Scanner.MainScanner import MainScanner
from Scanner.YahooScanner import YahooScanner
from Trading.AccountManager.AccountManager import AccountManager
from Trading.OrdersSender.OrderSender import OrderSender
from Trading.Strategy.BasicStrategy import BasicStrategy
from Trading.Strategy.CloserStrategy import CloserStrategy
from Trading.TraderManager.TraderManager import TraderManager
from Trading.TraderStrategy.SmartTrader import SmartTrader

config = load_configuration('./Config/config.json')
order_sender_config = config.order_sender_config

trader_client = TradingClient(api_key=order_sender_config.api_key,
                              secret_key=order_sender_config.api_secret,
                              paper=True)

yahoo_puller = YahooDataPuller(config.yahoo_config)
all_scanners = [FinvizScanner(config.finviz_config)]
specific_scanners = [YahooScanner(yahoo_puller)]
account_manager = AccountManager(trader_client)
main_scanner = MainScanner(specific_scanners, all_scanners)
order_sender = OrderSender(account_manager, trader_client)
strategy = BasicStrategy(yahoo_puller, account_manager)
close_strategy = CloserStrategy(account_manager)
trader = SmartTrader(strategy, order_sender)
close_trader = SmartTrader(close_strategy, order_sender)
trader_manager = TraderManager(main_scanner, trader, close_trader, account_manager, config.default_scanner_settings)

while True:
    if datetime.now().hour >= 6:
        trader_manager.trade_according_to_scanner()

    time.sleep(60 * 60 * 24)

