from wdig.database import Transaction


def map_to_mortgage_budget(tran: Transaction) -> None:
    budget_tag = None

    if 'CASEY & MIHEE LOAN PAYMT' in tran.description.upper():
        budget_tag = 'mortgage'

    if budget_tag:
        tran.budget_tag = budget_tag
        tran.budget_category = 'mortgage'
        return True
