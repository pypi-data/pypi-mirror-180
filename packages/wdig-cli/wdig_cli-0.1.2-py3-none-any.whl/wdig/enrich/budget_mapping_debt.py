from wdig.database import Transaction


def map_to_debt_budget(tran: Transaction) -> None:
    budget_tag = None

    if 'jebu coop' in tran.description.lower():
        budget_tag = 'cc payments'

    if 'ACCOUNT FEE' in tran.description.upper():
        budget_tag = 'bank fees'

    if 'DD DISHONOUR FEE' in tran.description.upper():
        budget_tag = 'bank fees'

    if 'DRAFT INTEREST' in tran.description.upper():
        budget_tag = 'bank fees'

    if budget_tag:
        tran.budget_tag = budget_tag
        tran.budget_category = 'debt'
        return True
