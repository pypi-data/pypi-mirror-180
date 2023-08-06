from wdig.database import Transaction
from fnmatch import fnmatch


def map_to_donations_budget(tran: Transaction) -> None:
    budget_tag = None

    for m in [
        'Salvation Army NZ*',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'salvation army'

    for m in [
        'PAYPAL *KIVA.ORG*',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'kiva'

    for m in [
        '*OREWA BAPTIST CHURCH*',
        'Orewa Baptist Church*',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'church'

    for m in [
        'AUCKLAND CITY MISSION*'
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'city mission'

    if budget_tag:
        tran.budget_tag = budget_tag
        tran.budget_category = 'donations'
        return True
