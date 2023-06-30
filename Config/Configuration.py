from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase

from Config.Configs.FinvizConfig import FinvizConfig
from Config.Configs.OrderSenderConfig import OrderSenderConfig
from Config.Configs.YahooConfig import YahooConfig


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class Configuration:
    order_sender_config: OrderSenderConfig
    finviz_config: FinvizConfig
    yahoo_config: YahooConfig
    default_scanner_settings: dict
