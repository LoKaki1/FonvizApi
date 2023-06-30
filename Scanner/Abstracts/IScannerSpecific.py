
class IScannerSpecific:
    name: str

    def scan(self,
             tickers: list[str]) -> list[str]:
        """
        :param tickers:
        :return:
        """