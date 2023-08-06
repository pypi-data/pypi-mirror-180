from sqlalchemy import true
from wdig.database import Transaction
from fnmatch import fnmatch


"""
map transactions to budget items

flag transactions as "not matched" if not mapped to budget

list of rules? we can infer category by mapping budget item to category.

are we just mapping merchants to budget items? no - we don't have to map everything.

SUMMARY SPREADSHEET:

category, budget item, amount
-----------------------------
period, fixed, school fees, $amount, $budget,
fixed, power, $xxx
unknown, unknown, $xxx


car tax	$11.67
car wof & maint	$50.00
tkd oong bus	$23.33

"""


def map_to_fixed_budget(tran: Transaction) -> None:
    budget_tag = None

    if 'orcon' in tran.description.lower():
        budget_tag = 'orcon'

    if 'southern cross' in tran.description.lower():
        budget_tag = 'southern cross'

    if 'auckland council' in tran.description.lower():
        budget_tag = 'city council'

    if 'fidelity life' in tran.description.lower():
        budget_tag = 'life insurance'

    for m in [
        "*enviro waste*",
        "*ENVIROWASTE*",
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'recycling'

    for m in [
        "*PAY King's way primary school*",
        "*PAY Kingsway*",
        '*NZ CHRISTIAN PROPRIE*',
        'NZCPT kingsway*',
        'Kingsway Fees James JEONG-BURNS',
        'NZCPT*',
        '*CHRISTIAN PROPRIETORS*',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'school fees'

    for m in [
        'PAY kingsway special donation acc ;',
        'Kingsway SC James JEONG-BURNS',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'school special character'

    if 'CONTACT ENERGY' in tran.description.upper():
        budget_tag = 'power'

    if 'watercare' in tran.description.lower():
        budget_tag = 'water'

    if 'aa insurance' in tran.description.lower():
        if tran.amount < -100:
            budget_tag = 'home insurance'
        else:
            budget_tag = 'car insurance'

    if 'lastpass.com' in tran.description.lower():
        budget_tag = 'password vault'

    for m in [
        "Microsoft*Realms*",
        "*MICROSOFT*REALMS*",
        "*MOJANG*",
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'minecraft realm'

    if 'apple.com' in tran.description.lower():
        budget_tag = 'apple'

    for m in [
        "GOOGLE*Google Stor*",
        "GOOGLE*YouTubePrem*",
        'Google*Storage*',
        'GOOGLE YouTube*',
        'Google YouTubePremiu*',
        'YouTubePremium*',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'google storage+youtube'

    for m in [
        "*PAY Red Beach playcentre*",
        "*RBLC*",
        "PAY Orewa beach kindy*",
        'orewa beach kindy James JB',
        'Orewa Kindy James JB',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'kindy'

    if 'AMAZON MUSIC UNLIMIT' in tran.description.upper():
        budget_tag = 'amazon music'

    if 'vodafone prepay' in tran.description.lower():
        budget_tag = 'mobile usage'

    if 'snap fitness' in tran.description.lower():
        budget_tag = 'casey gym'

    if 'crashplan' in tran.description.lower():
        budget_tag = 'backup'

    if 'disney plus' in tran.description.lower():
        budget_tag = 'disney'

    if 'blake elearning' in tran.description.lower():
        budget_tag = 'reading eggs'

    for m in [
        'Fixed Expenses Taekwondo*',
        'daehan tkd*',
        'Daehan TKD*',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'tkd'

    if 'microsoft*store' in tran.description.lower():
        budget_tag = 'onedrive'
    if 'microsoft*onedrive' in tran.description.lower():
        budget_tag = 'onedrive'

    if 'northern arena' in tran.description.lower():
        budget_tag = 'swim lessons'

    if 'netflix' in tran.description.lower():
        budget_tag = 'netflix'

    if 'netflix' in tran.description.lower():
        budget_tag = 'netflix'
# EA *ORIGIN.COM help.ea.com ;

    if budget_tag:
        tran.budget_tag = budget_tag
        tran.budget_category = 'fixed'
        return True


# PAY Daehan tkd ;
