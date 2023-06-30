from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase

from Config.Configs.Abstracts.ApiConfig import ApiConfig


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class FinvizConfig(ApiConfig):
    """

    """