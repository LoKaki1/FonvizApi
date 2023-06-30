import requests

from Common.Common import _format_price
from Common.Logger.Logger import logger_info_decorator, log_info
from Config.Configs.YahooConfig import YahooConfig
from Pullers.StocksDataPuller.IStocksDataPuller import IStocksDataPuller


class YahooDataPuller(IStocksDataPuller):

    def __init__(self, config: YahooConfig):
        self.url = config.url
        self.headers = config.headers
        self.formatting = lambda result, time_in_candle, index: _format_price(result.json()['chart']['result'][0]
                                                       ['indicators']['quote'][0][time_in_candle][index])

    @logger_info_decorator
    def get_price(self, ticker: str, time_in_candle: str, index: int, **kwargs) -> float:
        kwargs.update(ticker=ticker)
        url = self.url.format(**kwargs)
        yahoo_result = requests.get(url, headers=self.headers)
        log_info(yahoo_result.json())

        return self.__format_result(yahoo_result, time_in_candle, index)

    @logger_info_decorator
    def __format_result(self, result, time_in_candle: str, index: int) -> float:
        try:
            return self.formatting(result, time_in_candle, index)
        except Exception:
            raise Exception("Something went wrong 😁 while formatting")
