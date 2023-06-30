from Config.ConfigurationLoader import load_configuration
from Pullers.StocksDataPuller.YahooDataPuller import YahooDataPuller
from Scanner.FinvizScanner import FinvizScanner
from Scanner.MainScanner import MainScanner
from Scanner.YahooScanner import YahooScanner
from Trading.OrdersSender.OrderSender import OrderSender
from Trading.Strategy.BasicStrategy import BasicStrategy
from Trading.TraderManager.TraderManager import TraderManager
from Trading.TraderStrategy.SmartTrader import SmartTrader

config = load_configuration('./Config/config.json')

yahoo_puller = YahooDataPuller(config.yahoo_config)
all_scanners = [FinvizScanner(config.finviz_config)]
specific_scanners = [YahooScanner(yahoo_puller)]

main_scanner = MainScanner(specific_scanners, all_scanners)
order_sender = OrderSender(config.order_sender_config)
strategy = BasicStrategy(yahoo_puller)
trader = SmartTrader(strategy, order_sender)
trader_manager = TraderManager(main_scanner, trader, config.default_scanner_settings)

trader_manager.trade_according_to_scanner()
