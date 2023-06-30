from typing import Union, Callable, Any

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

from Common.Logger.Logger import logger_info_decorator
from Config.Configs.OrderSenderConfig import OrderSenderConfig
from Trading.OrdersSender.IOrderSender import IOrderSender


class OrderSender(IOrderSender):
    borders_expressions: dict[str, Union[Callable[[Any], dict[str, Any]], Callable[[Any], dict[str, Any]]]]

    def __init__(self, order_sender_config: OrderSenderConfig):
        self.trading_client = TradingClient(api_key=order_sender_config.api_key,
                                            secret_key=order_sender_config.api_secret,
                                            paper=True)
        self.borders_expressions = {
            'stop_loss': lambda stop_price: {'stop_price': stop_price,
                                             'limit_price': stop_price},
            'take_profit': lambda limit_price: {'limit_price': limit_price}
        }

    @logger_info_decorator
    def send_limit_order(self,
                         ticker: str,
                         type_of_order: str,
                         quantity: int,
                         price: float,
                         stop_loss: float,
                         take_profit: float):
        order_type = OrderSide(type_of_order)
        borders = self.__check_borders(stop_loss, take_profit)
        limit_order_data = LimitOrderRequest(
            symbol=ticker,
            qty=quantity,
            limit_price=price,
            side=order_type,
            time_in_force=TimeInForce.DAY,
            **borders
        )

        return self.trading_client.submit_order(order_data=limit_order_data)

    @logger_info_decorator
    def make_market_order(self,
                          ticker: str,
                          type_of_order: str,
                          quantity: int,
                          stop_loss: float,
                          take_profit: float):
        order_type = OrderSide(type_of_order)
        borders = self.__check_borders(stop_loss, take_profit)
        market_order_data = MarketOrderRequest(
            symbol=ticker,
            qty=quantity,
            side=order_type,
            time_in_force=TimeInForce.DAY,
            **borders
        )
        # Market order
        market_order = self.trading_client.submit_order(
            order_data=market_order_data
        )

        return market_order

    @logger_info_decorator
    def __check_borders(self, stop_price: float, take_profit: float):
        return {
            'stop_loss': self.__check_border(stop_price, 'stop_loss'),
            'take_profit': self.__check_border(take_profit, 'take_profit')
        }

    @logger_info_decorator
    def __check_border(self, border: float, type_of_border: str):
        if border is None:
            return {type_of_border: None}

        border_expression = self.borders_expressions[type_of_border](border)

        return border_expression
