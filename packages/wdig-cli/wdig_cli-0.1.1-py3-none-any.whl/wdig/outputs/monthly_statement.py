"""
MS is a P&L summary for the month
 - gross income
 - expenses by categry vs budget
 - remaining

purpose is to see:
 - did we spend less then we earnt in that month? and by how much
 - are our budgets accurate

this is something that is only useful retrospectivily.  not good for tracking progress.

by period? -- calandar for now


LAYOUT

title (from to dates)
messages (i.e. transfers not zero)

table:
 income, amount, budget, remaining, %
 category, amount, budget, remaining, %
 remaining, amount, budget, remaining, %

"""


# get the data in the right structure
# pop it on a gsheet

from dataclasses import dataclass
from typing import List
from sqlalchemy import extract, func
from wdig.database import Transaction, DatabaseAppSession
from wdig.google_sheets import get_transaction_sheet, _create_or_replace_worksheet


month = 5
year = 2022

# TODO group by period_year and period_month
db = DatabaseAppSession()
trans = db.db_session.query(
        Transaction.category,
        func.sum(Transaction.amount),
        func.count(Transaction.tran_id)) \
    .filter(
        Transaction.is_duplicate == False,  # noqa E712
        extract('year', Transaction.tran_date) == year,
        extract('month', Transaction.tran_date) == month) \
    .group_by(Transaction.category) \
    .all()


# TODO read this from the budget sheet
# bank fees includes debt
budget = {'income': 9600, 'fixed': -1798.74, 'variable': -3108.33, 'mortgage': -2594.98, 'savings': -950, 'donation': -293.33, 'bank fees': -95, 'debt': -340}


@dataclass
class CategorySummary:
    category: str
    actual: float
    budget: float
    remaining: float
    percentage: int

    def as_list(self) -> List:
        return [self.category, self.actual, self.budget, self.remaining, self.percentage]

@dataclass
class Statement:
    title: str
    message: List[str]
    income: CategorySummary
    expense_summaries: List[CategorySummary]


data = Statement(
    title='Monthly Statement',
    message='',
    income=None,
    expense_summaries=[]
)


for tran in trans:
    if tran[0] == 'transfer':
        data.message = f'transfers should be zero -- {tran[1]}'
        continue

    cat_budget = budget[tran[0]]
    amount = float(tran[1])
    cs = CategorySummary(
        category=tran[0],
        actual=amount,
        budget=cat_budget,
        remaining=amount - cat_budget,
        percentage=(amount / cat_budget)
    )

    if tran[0] == 'income':
        data.income = cs
    else:
        data.expense_summaries.append(cs)

# TODO add remaining amount line


sheet = get_transaction_sheet()
worksheet = _create_or_replace_worksheet(sheet, f'{month} statement', rows=50)
worksheet.update('A1', data.title)
worksheet.update('A2', data.message)

worksheet.update('A4', [['category', 'actual', 'budget', 'remaining', '%']])
worksheet.update('A5', [data.income.as_list()])

for idx, cat in enumerate(data.expense_summaries):
    worksheet.update(f'A{7 + idx}', [cat.as_list()])
pass
