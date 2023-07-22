class IOrderSender:

    def send_limit_order(self,
                         ticker: str,
                         type_of_order: str,
                         quantity: int,
                         price: float,
                         stop_loss: float = None,
                         take_profit: float = None):
        """
        :param ticker:
        :param type_of_order:
        :param quantity:
        :param price:
        :param stop_loss:
        :param take_profit:
        :return:
        """

    def make_market_order(self,
                          ticker: str,
                          type_of_order: str,
                          quantity: int,
                          stop_loss: float = None,
                          take_profit: float = None):
        """
        :param ticker:
        :param type_of_order:
        :param quantity:
        :param stop_loss:
        :param take_profit:
        :return:
        """