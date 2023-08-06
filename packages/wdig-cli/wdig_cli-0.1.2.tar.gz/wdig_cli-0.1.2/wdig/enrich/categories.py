from fnmatch import fnmatch
from wdig.database import Transaction
from wdig.queries import get_tran_by_id


"""

variable	unknown	M Jeng 	-$1,000.00

"""


def apply_category_to_tran(tran_id: str) -> Transaction:
    tran = get_tran_by_id(tran_id)
    apply_category(tran)
    return tran


def apply_category(tran: Transaction) -> None:
    if _is_transfer(tran.description, tran.account_format, tran.original_columns.get('Type'), tran.original_columns.get('Details')):
        tran.category = 'transfer'
    elif _is_income(tran.description):
        tran.category = 'income'
    elif _is_interest(tran.description):
        tran.category = 'interest'
    elif _is_donation(tran.description):
        tran.category = 'donation'
    elif _is_mortgage(tran.description):
        tran.category = 'mortgage'
    elif _is_saving(tran.description):
        tran.category = 'savings'
    elif _is_bank_fee(tran.description):
        tran.category = 'bank fees'
    elif _is_fixed(tran.description):
        tran.category = 'fixed'
    elif _is_debt(tran.description):
        tran.category = 'debt'
    elif _is_tax(tran.description):
        tran.category = 'tax'
    else:
        tran.category = 'variable'


def _is_tax(description: str) -> bool:
    return 'INLAND REVENUE' in description


def _is_transfer(description, account_format, original_type, original_details) -> None:

    if description in [
        '4367-****-****-7631 Debit Transfer',
        'Jebu ANZ transfer',
        'Fixed Expenses fixed exp',
        'AP#20154352 TO M.JEONG ;Bnz revolvin',
        'TRANSFER TO C BURNS  M JEONG - 16 ;',
        'Cashback Visa Gold  ',
        'TRANSFER TO C BURNS  M JEONG - 08 ;',
        'TRANSFER FROM C BURNS  M JEONG - 08 ;',
        'TRANSFER FROM C BURNS  M JEONG - 09 ;',
        'TRANSFER TO C BURNS  M JEONG - 09 ;',
        'TRANSFER FROM C BURNS  M JEONG - 16 ;',
        'Revolving Mortgage',
        'CASEY & MIHEE cash',
        'Burns C Transfer ',
        'CASEY & MIHEE fixed exp',
        'C BURNS  M JEONG Bnz revolvin',
        'CASEY & MIHEE cash',
        'C Burns  M Jeong Anz Credit Acc',
        'Revolving Mortgage ',
        'Fixed Expenses ',
        'Mihee Anz Jebu ',
        'Cash cash',
        'JEBU ANZ ANZ JEBU',
        'Online       Payment -  Thank You ',
        'Automatic Payment - Thank You ',
        'Direct Credit jebu bnz MIHEE ;Ref: jebu bnz MIHEE',
        'Direct Credit JEBU A MIHEE ;Ref: JEBU A MIHEE',
        'Cash ',
        'C Burns  M Jeong From Kiwibank',
        'AP#15249025 FROM C BURNS  M JEONG ;Transfer from C BURNS  M JEONG - 09',
        '4367-****-****-7631 Credit Transfer',
        'PAY M jeong ;ANZ credit Acc',
        'AP#15249025 TO C BURNS  M JEONG ;Transfer to C BURNS  M JEONG - 08',
        'PAY ANZ Cash Account ;To ANZ',
        'TRANSFER FROM M JEONG - 00 ;'
    ]:
        return True
    else:
        return False  # why care about transfers? they are hard to categorize. they should equal 0.

    if account_format == "anz-csv":
        if original_type == "Transfer":
            return True
        if (original_type == "Bill Payment" and original_details == "C Burns  M Jeong"):
            return True
        if (original_type == "Automatic Payment" and original_details == "Cashback Visa Gold"):
            return True

    if account_format == "kiwibank-csv":
        for p in [
            "TRANSFER FROM C BURNS M JEONG - 09*",
            "*AP#15249025 FROM C BURNS*M JEONG ;Transfer from C BURNS  M JEONG - 09*",
            "AP#14783586 TO JEBU BNZ ;jebu kb transfer*",
            "AP#15249025 TO C BURNS  M JEONG ;Transfer to C BURNS  M JEONG - 08*",
            "TRANSFER TO C BURNS  M JEONG - 08*",
            "PAY ANZ Cash Account ;To ANZ",
            "AP#16085738 TO ANZ CASH ACCOUNT ;To ANZ*",
            "PAY ANZ Cash Account ;To ANZ*",
            "AP#16085738 TO ANZ CASH ACCOUNT ;To ANZ*",
            "PAY M jeong ;ANZ credit Acc*",
            "Bill Payment BURNS CASEY*",
            "Jebu Kiwibank*",
            "TRANSFER*BURNS*JEONG - 09*",
            "TRANSFER FROM*BURNS*JEONG*09*",
            "TRANSFER FROM*BURNS*JEONG*08*",
            "TRANSFER TO*BURNS*JEONG*16*",
            "TRANSFER FROM*BURNS*JEONG*16*",
            "PAY M JEONG*",
        ]:
            if fnmatch(description, p):
                return True

    if account_format == "anz-cc-csv":
        if original_details in [
            "Automatic Payment - Thank You ",
            "Online       Payment -  Thank You ",
        ]:
            return True

    for p in [
        'AP#20154352',  # to BNZ revolving
        'C BURNS  M JEONG Bnz revolvin',  # received bnz revolving ap
        'PAY M.jeong ;Bnz revolvin'
    ]:
        if p in description:
            return True


def _is_income(description: str) -> bool:
    for p in [
        "Salary*",
        "*FROM ONEHUNGA TOY LIBRARY*",
        "*Direct Credit FRAEDOM*",
        "*Autocashbacks*",
        "TRANSFER FROM*JEONG*00*",
        'Polyglot Group Pty*',
        'Direct Credit*I.R.D.*',
        'Jeong Chang Weon 22228180737C S000 Imt',
    ]:
        if fnmatch(description, p):
            return True


def _is_interest(description: str) -> bool:
    for p in ["*INTEREST DEBIT*", "*Interest*", "*INTEREST*"]:
        if fnmatch(description, p):
            return True


def _is_mortgage(description: str) -> bool:
    for p in [
        "*JEBU WESTPAC*",
        "*lump sum pmt*",
        "*Direct Credit from westpac Burns*",
        "*Lump Sum Payment*",
        "*TO JEBU BNZ ;jebu kb transfer*",  # AP to BNZ
        "*AP#15260870 TO C BURNS M JEONG*",  # new house mortgage
        "*AP#15260872 TO C BURNS M JEONG*",  # new house mortgage
        "AP#15260870 TO C BURNS  M JEONG ;Transfer to C BURNS  M JEONG - 14",
        "AP#15260872 TO C BURNS  M JEONG ;Transfer to C BURNS  M JEONG - 15",
        "AP#16085738 TO ANZ CASH ACCOUNT ;To ANZ",
        "AP#16085738 TO ANZ CASH ACCOUNT ;To ANZ",
        "MANUAL LOAN PAYMENT*",
        'CASEY & MIHEE LOAN PAYMT*',
        '*LOAN FUNDS*',
        'Discharge NA*',
        'Home Loan ',
        '1212/2120000000/002 SOLICITOR',
        'Direct Credit Refinance The Legal Team*',

    ]:
        if fnmatch(description, p):
            return True


def _is_donation(description) -> bool:
    for p in [
        "VICTORY CHURCH",
        "Salvation Army",
        "KIVA",
        "Victory church",
        "KIVA.ORG",
        "PAY NZ Victory church",
        "AUCKLAND CITY MISSION",
        "AP#18688032 TO OREWA BAPTIST CHURCH",
        'AP#20400921 TO OREWA BAPTIST CHURCH',
        'Orewa Baptist Church*',
        'AUCKLAND CITY*',
    ]:
        if p in description:
            return True


def _is_saving(description) -> bool:
    for p in [
        "*KIWI WEALTH KIWISAVER SCHEME*",
        "*OONG SAVINGS*",
        "*SAN SAVINGS*",
        "*SMARTSHARES*",
        "*Sharesies*",
        "*SHARESIES*",
        'SUPERLIFE WORKPLACE*',
        'Kiwibank savings kb savings'
    ]:
        if fnmatch(description, p):
            return True


def _is_bank_fee(description) -> bool:
    for p in [
        # '*conversion rate*', # not always fees
        "*Monthly A/C Fee*",
        "*OTHER BANK ATM FEE*",
        "*VisaDebitAnnualFee*",
        "*REPLACEMENT ATM/EFTPOS*",
        "INTEREST DEBIT*" "*Unarranged Overdraft Fee*",
        "REPLACEMENT ATM/EFTPOS*",
        "VisaDebitAnnualFee*",
        "*DISHONOUR FEE*",
        "CLOSE O'DRAFT INTEREST",
        '*ACCOUNT FEE*',
        '*Joint/Additional Account Fee*',
        'Account Fee*',
    ]:
        if fnmatch(description, p):
            return True


def _is_fixed(description) -> bool:
    for p in [
        "*Netflix.Com*",
        "*Contact Energy Ltd Wellington Nz*",
        "*Northern Arena Silverdale Nz*",
        "*ENVIRO WASTE SERVICES LIMITED*",
        "*Vodafone Prepay*",
        "*PAY Red Beach playcentre*",
        "*PAY King's way primary school*",
        "*Snap Fitness Newstead*",
        "*Direct Debit -AUCKLAND CITY COUNCIL*",
        "*PAY orewa beach kindergarten*",
        "*Direct Debit -FIDELITY LIFE ASSURANCE*",
        "*Direct Debit -SOUTHERN CROSS MEDICAL*",
        "*AP#13629838 TO ORCON INTERNET*",
        "*AMAZON MUSIC UNLIMITED SYDNEY*",
        "*PAY Global Martial Art*",
        "*Watercare Services*",
        "*Northern Arena Limit*",
        "*LIGHTBOX AUCKLAND*",
        "*Aa Insurance Auckland Nzl*",
        "*GOOGLE Music g.co/helppay*",
        "*PAY CONTACT ENERGY ;BURNSC 500365729 KIWIBANK*",
        "*Aa Insurance*",
        "*APPLE.COM/BILL SYDNEY*",
        "*MICROSOFT*REALMS PLUS MMSBILL.INFO*",
        "*NEW ZEALAND CHRISTIAN PROPRIETORS TRUST*",
        "*CONTACT ENERGY*",
        "*FIDELITY LIFE*",
        "*Watercare Online*",
        "*Ezi*Snap Fitness*",
        "*Crashplan*",
        "*MOJANG*",
        "*RBLC*",
        "*PAY WATERCARE SERVICES*",
        "*PAY Kingsway*",
        "PAY Daehan tkd*",
        "Microsoft*Realms*",
        "*Sports4Tot*",
        "PAY Joseph*",
        "Neon*",
        "Contact Energy*",
        "PAY Orewa beach kindy*",
        "Orcon*",
        'Disney PLUS*',
        'AUCKLAND COUNCIL*',
        '*NZ CHRISTIAN PROPRIE*',
        'NZCPT kingsway*',
        'Microsoft*Store*',
        '*SNAP FITNESS*',
        '*EZIDEBIT FOR AUCKLAND CITY COUNCIL*',
        'Daehan TKD Ethan JB TKD',
        'PAY kingsway special donation acc ;',
        'DRI*CrashPlan for SB 557268497805',
        'Blake eLearning NZD Leichhardt ;',
        'NETFLIX.COM 57268497805',
        'Disney Plus 57268497805',
        'AMAZON MUSIC UNLIMIT 557268497805',
        'MICROSOFT*REALMS 1 M 57268497805',
        'APPLE.COM/BILL 57268497805',
        'orewa beach kindy James JB',
        'Microsoft*OneDrive S 57268497805',
        'Southern Cross Healt ',
        'Fixed Expenses Taekwondo fe',
        'AA INSURANCE 57268497805',
        'Kingsway Fees James JEONG-BURNS',
        'Kingsway SC James JEONG-BURNS',
        'Snap Fitness Albany    Albany        Nz ',
        'Google Storage Auckland*',
        'YouTubePremium Auckland*',
        'Netflix New Zealand 57268497805',
        'Orewa Kindy James JB',
        'LastPass.com*',
        'Auckland Council*',
        'Google YouTubePremiu 57268497805',
        'NZCPT*',
    ]:
        if fnmatch(description, p):
            return True


def _is_debt(description) -> bool:
    for p in [
        'AP#19180516 TO ASB JEBU ;ASB Transfer',
        'TRF*4327*6018*',
        'AP#20181673*',  # coop CC
        'jebu coop*',
    ]:
        if fnmatch(description, p):
            return True


if __name__ == '__main__':
    tran = apply_category_to_tran('574210f1-1184-ca63-ddbd-42f0fd21323e')
    print(tran.category)
    pass
