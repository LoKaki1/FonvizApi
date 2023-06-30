import requests

from Common.Common import _format_price

YAHOO_INTERDAY_API = "https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?region=US&lang=en-US&includePrePost=false&interval={interval}&useYfid=true&range={_range}&corsDomain=finance.yahoo.com&.tsrc=finance"
USER_AGENT = 'user-agent'
USER_AGENT_VALUE = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple WebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 "

class YahooAPI:

    def __init__(self):
        self.yahoo_api = YAHOO_INTERDAY_API
        self.headers = {USER_AGENT: USER_AGENT_VALUE}

    def get_first_price(self, ticker: str) -> float:
        data = requests.get(self.yahoo_api.format(ticker=ticker, interval='5m', _range='1d'),
                            headers=self.headers)

        try:
            return _format_price(data.json()['chart']['result'][0]['indicators']['quote'][0]['open'][0])
        except Exception:
            raise Exception("Something went wrong 😁")

    def get_last_price(self, ticker: str) -> float:
        data = requests.get(self.yahoo_api.format(ticker=ticker, interval='1m', _range='1d'),
                            headers=self.headers)

        return _format_price(data.json()['chart']['result'][0]['indicators']['quote'][0]['close'][-1])

    def is_finished_bigger(self, ticker) -> bool:
        try:
            open_price = self.get_first_price(ticker)
            close_price = self.get_last_price(ticker)

            return close_price > open_price

        except Exception:

            return False
