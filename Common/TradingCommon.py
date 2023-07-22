from datetime import datetime
from datetime import date, timedelta
import pandas_market_calendars as mcal


open_trade_time = datetime.strptime('16:30:00', '%H:%M:%S').time()
close_trade_time = datetime.strptime('23:00:00', '%H:%M:%S').time()

open_premarket = datetime.strptime('11:00:00', '%H:%M:%S').time()
close_after_hours = datetime.strptime('03:00:00', '%H:%M:%S').time()


def is_trading_time() -> bool:
    return open_trade_time < datetime.now().time() < close_trade_time


def can_i_even_trade() -> bool:
    return (open_premarket < (now := datetime.now().time()) or now < close_after_hours) and 1 < datetime.now().weekday() < 7
