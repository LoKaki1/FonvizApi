import requests

class FinvizApi:

    def __init__(self):
        self.url = 'https://finviz.com/screener.ashx?v=411&f'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

    def get_stocks(self, **kwargs):
        data = requests.get(self.url, params=kwargs, headers=self.headers)

        if data.status_code == 200:
            data = data.text.split('<!-- TS')[1].split('TE -->')[0]

            stocks = [stock.split('|') for stock in data.split('\n')]

            return stocks

        return data


finviz_api = FinvizApi()

print(finviz_api.get_stocks(f='sh_price_u15'))

