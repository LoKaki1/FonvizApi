from Common.Logger.Logger import logger_info_decorator, log_info
from Pullers.StocksDataPuller.IStocksDataPuller import IStocksDataPuller
from Scanner.Abstracts.IScannerSpecific import IScannerSpecific


class YahooScanner(IScannerSpecific):

    def __init__(self, stocks_data_puller: IStocksDataPuller):
        self.stocks_data_puller = stocks_data_puller
        self.name = 'yahoo'

    @logger_info_decorator
    def scan(self,
             tickers: list[str]) -> list[str]:
        return [
            ticker for ticker in tickers if self._is_ticker_valid(ticker)
        ]

    @logger_info_decorator
    def _is_ticker_valid(self, ticker: str):
        try:
            open_price = self.__get_open(ticker)
            close_price = self.__get_close(ticker)

            return close_price > open_price

        except Exception as e:
            log_info(e)

            return False

    @logger_info_decorator
    def __get_open(self, ticker: str):
        return self.stocks_data_puller.get_price(ticker, 'open', 0, interval='1m', _range='1d')

    @logger_info_decorator
    def __get_close(self, ticker: str):
        return self.stocks_data_puller.get_price(ticker, 'close', -1, interval='1m', _range='1d')