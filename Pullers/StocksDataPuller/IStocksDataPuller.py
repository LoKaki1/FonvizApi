class IStocksDataPuller:

    def get_price(self, ticker: str, time_in_day: str, index: int, **kwargs) -> float:
        """
        :param index:
        :param time_in_day:
        :param ticker:
        :param kwargs:
        :return:
        """
