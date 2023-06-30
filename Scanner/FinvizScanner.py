import requests

from Common import Common
from Common.Logger.Logger import logger_info_decorator
from Config.Configs.FinvizConfig import FinvizConfig
from Scanner.Abstracts.IScannerEverything import IScannerEverything


class FinvizScanner(IScannerEverything):

    def __init__(self,
                 config: FinvizConfig):
        self.config = config
        self.name = 'finviz'

    @logger_info_decorator
    def scan(self, **kwargs):

        data = requests.get(self.config.url, params=kwargs, headers=self.config.headers)

        if data.status_code == 200:
            data = data.text.split('<!-- TS')[1].split('TE -->')[0]

            stocks = Common.remove_from_list_list([Common.remove_empty(stock.split('|'))
                                                   for stock in data.split('\n')
                                                   ])
            stocks = [stock[0] for stock in stocks]

            return stocks

        raise AssertionError(data.content)
