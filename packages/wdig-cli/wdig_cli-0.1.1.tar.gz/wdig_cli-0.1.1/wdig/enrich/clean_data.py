from wdig.database import Transaction, DatabaseAppSession
from sqlalchemy import func
from rich.console import Console

console = Console()


def dedup():
    db_conn = DatabaseAppSession()
    duplicated_tran_ids = (
        db_conn.db_session.query(Transaction.tran_id)
        .group_by(Transaction.tran_id)
        .having(func.count(Transaction.tran_id) > 1)
    )

    with console.status(f"[bold green]Deduping duplicate transactions...") as status:
        dup_count = 0
        for dup in duplicated_tran_ids:
            dup_trans = (
                db_conn.db_session.query(Transaction)
                .filter(Transaction.tran_id == dup.tran_id)
                .order_by(Transaction.imported_date.desc())
            )

            most_recent_file_name = ""
            for dup_tran in dup_trans:
                if most_recent_file_name == "":
                    most_recent_file_name = dup_tran.file_name

                if dup_tran.file_name != most_recent_file_name:
                    dup_tran.is_duplicate = True
                    dup_count += 1

                db_conn.db_session.commit()
    console.print(f'Deduped duplicate transactions')

    return dup_count


if __name__ == "__main__":
    dedup()
