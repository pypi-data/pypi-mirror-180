from wdig.database import Transaction
from fnmatch import fnmatch


def map_to_savings_budget(tran: Transaction) -> None:
    budget_tag = None

    for m in [
        'M Jeng*',
        'Kiwibank savings kb savings*',
        'Direct Debit -SMARTSHARES LIMITED*',
        'SUPERLIFE WORKPLACE*',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'savings'

    if budget_tag:
        tran.budget_tag = budget_tag
        tran.budget_category = 'savings'
        return True
