import uuid
from sqlalchemy.sql.expression import and_
from wdig.database import Transaction, DatabaseAppSession
from datetime import datetime as dt
from rich.progress import track
from rich.console import Console
from wdig.enrich.periods import apply_period


console = Console()

# 20000	debit	BNZ Revolving Mortgage	BNZ	d013e510-9570-5eae-7c66-b1201cd726fb
# 26353.52	credit	Kiwibank Cash	Kiwibank	ec169870-b45a-4679-e832-620194f3e76c
# 575000	debit	BNZ Revolving Mortgage	BNZ	707654c7-fc23-f2c5-2d4d-d37aadb10eeb
# variable -595000	debit	BNZ Revolving Mortgage	BNZ	aa31bc69-066a-c6fa-fcc7-d4aa37e76829

_adjustments = [
    {
        "amount": -20000,
        "category": "mortgage",
        "reason": "mortgage transfer for d013e510-9570-5eae-7c66-b1201cd726fb",
        "month": "1",
        "year": 2022,
    },
    {
        "amount": -26353.52,
        "category": "mortgage",
        "reason": "mortgage transfer for ec169870-b45a-4679-e832-620194f3e76c",
        "month": "1",
        "year": 2022,
    },
    {
        "amount": -575000,
        "category": "mortgage",
        "reason": "mortgage transfer for 707654c7-fc23-f2c5-2d4d-d37aadb10eeb",
        "month": "1",
        "year": 2022,
    },
    {
        "amount": 595000,
        "category": "mortgage",
        "reason": "mortgage transfer for aa31bc69-066a-c6fa-fcc7-d4aa37e76829",
        "month": "1",
        "year": 2022,
    },
    {
        "amount": 3078,
        "category": "transfer",
        "reason": "cc payment split over month end",
        "month": "2",
        "year": 2021,
    },
    {
        "amount": -3078,
        "category": "transfer",
        "reason": "cc payment split over month end",
        "month": "3",
        "year": 2021,
    },
    {
        "amount": 3078,
        "category": "transfer",
        "reason": "cc payment split over month end",
        "month": "7",
        "year": 2021,
    },
    {
        "amount": -3685.44,
        "category": "transfer",
        "reason": "cc payment split over month end",
        "month": "8",
        "year": 2021,
    },

]


def apply_adjustments() -> int:
    adjustment_tag_value = "adjustment"

    adjustment_count = 0
    for adj in track(_adjustments, description='Adding adjustments...'):
        db_conn = DatabaseAppSession()

        tran = (
            db_conn.db_session.query(Transaction)
            .filter(
                and_(
                    Transaction.tag == adjustment_tag_value,
                    Transaction.amount == adj["amount"],
                )
            )
            .first()
        )
        if not tran:
            tran = Transaction()
            db_conn.db_session.add(tran)
            adjustment_count += 1

        tran.tran_id = uuid.uuid4().hex
        tran.tran_type = "adjustment"
        tran.tag = adjustment_tag_value
        tran.amount = adj["amount"]
        tran.category = adj["category"]
        tran.account_name = "adjustment"
        tran.account_format = "adjustment"
        tran.account_number = "adjustment"
        tran.bank_name = "adjustment"
        tran.file_name = "adjustment"
        tran.original_columns = {}
        tran.imported_date = dt.now()
        tran.is_duplicate = False
        tran.tran_date = dt(year=int(adj["year"]), month=int(adj["month"]), day=19)
        tran.description = f'adjustment: {adj["reason"]}'
        apply_period(tran)

        db_conn.db_session.commit()

    console.print(f"added {adjustment_count} adjustments")
    return adjustment_count


if __name__ == '__main__':
    apply_adjustments()
