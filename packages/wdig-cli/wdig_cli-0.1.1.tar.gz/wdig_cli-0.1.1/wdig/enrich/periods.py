"""
transactions are allocated to periods, periods start around payday and can track spending until next pay day

example period: Aug 18th to Sept 17th -> `Aug 21`

plan is - support controlling spending by allocating budget amount to accounts on payday

what is our per-period spending per account?

"""

from datetime import datetime, timedelta
from wdig.database import Transaction


class Period():
    def __init__(self, date: datetime) -> None:
        # jan 1 > 15 --> dec peroid
        # jan 16 > end --> jan period

        if date.day < 16:
            date = date - timedelta(days=(date.day + 1))
        self._month = date.strftime('%m-%b')
        self._year = str(date.year)

    @property
    def year(self) -> str:
        return self._year

    @property
    def month(self) -> str:
        return self._month


def apply_period(tran: Transaction):
    # NOT USING PERIODS ANY MORE!
    # period = Period(tran.tran_date)
    tran.period_month = tran.tran_date.strftime('%m-%b')
    tran.period_year = str(tran.tran_date.year)
