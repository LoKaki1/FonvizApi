import datetime
import time
from typing import List, Any


def remove_empty(data: List[str]):
    for item in data:
        if item == '':
            data.remove(item)

    return data


def remove_from_list_list(data: List[List[Any]]):
    for item in data:
        if len(item) == 0:
            data.remove(item)

    return data


def _format_price(price) -> float:
    return float(str(price)[:5])


def sleep_untill(date: datetime.datetime):
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, t.day, date.hour, date.minute, date.second)

    if t.timestamp() > future.timestamp():
        future += datetime.timedelta(days=1)

    time.sleep((future-t).total_seconds())
