from wdig.database import Transaction


def map_to_income_budget(tran: Transaction) -> None:
    budget_tag = None

    if budget_tag:
        tran.budget_tag = budget_tag
        tran.budget_category = 'income'
        return True
