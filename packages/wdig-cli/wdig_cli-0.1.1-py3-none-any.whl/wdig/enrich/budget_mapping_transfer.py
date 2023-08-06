from wdig.database import Transaction


def map_to_transfer_budget(tran: Transaction) -> None:
    budget_tag = None

    if budget_tag:
        tran.budget_tag = budget_tag
        tran.budget_category = 'income'
        return True

# M Jeng
# AP#15260870 TO C BURNS  M JEONG ;Transfer to C BURNS  M JEONG - 14
# PAY M.jeong ;Bnz revolvin
# AP#15260870 TO C BURNS  M JEONG ;Transfer to C BURNS  M JEONG - 14
# AP#15260872 TO C BURNS  M JEONG ;Transfer to C BURNS  M JEONG - 15
# Revolving Mortgage Taekwondo fe
