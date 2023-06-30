from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class OrderSenderConfig:
    api_key: str
    api_secret: str
    quantity: int
