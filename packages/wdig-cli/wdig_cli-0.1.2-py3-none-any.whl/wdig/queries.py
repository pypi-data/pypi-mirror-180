from dataclasses import dataclass
from typing import List
import pandas as pd
from rich.console import Console
from datetime import timedelta, datetime
from wdig.database import DatabaseAppSession, Transaction
from sqlalchemy import text, func


console = Console()


def query_by_period(months_back: int = 6) -> pd.DataFrame:
    df = transactions_dataframe()
    date_param = (datetime.now() - timedelta(days=months_back*30)).strftime('%Y-%m-%d')
    df = df[df['tran_date'] > date_param]

    df_period = df[['period_month', 'period_year', 'amount']].groupby(['period_year', 'period_month']).agg(
        count=pd.NamedAgg(column='amount', aggfunc='count'),
        amount=pd.NamedAgg(column='amount', aggfunc='sum')
    )
    df_period.reset_index(inplace=True)
    df_period['amount'] = df_period['amount'].round(2)

    return df_period


def get_transaction_count() -> int:
    db_conn = DatabaseAppSession()
    stmt = db_conn.db_session.query(Transaction)
    tran_count = db_conn.db_session.query(Transaction).count()
    return tran_count


def transactions_dataframe() -> pd.DataFrame:
    db_conn = DatabaseAppSession()
    df = pd.read_sql_query(
        "select period_month, period_year, amount, category, budget_category, budget_tag, merchant_type, tag, account_name, description, id, tran_id, tran_type, account_number, tran_date, bank_name, account_format, imported_date, file_name from transaction where is_duplicate is false and category != 'transfer'",
        db_conn.db_engine.engine,
    )
    return df


def is_file_already_loaded(file_name: str) -> bool:
    db_conn = DatabaseAppSession()
    count = (
        db_conn.db_session.query(Transaction)
        .filter(Transaction.file_name == file_name)
        .count()
    )
    return count > 0


def get_unenriched_transaction_count() -> int:
    db_conn = DatabaseAppSession()
    count = (
        db_conn.db_session.query(Transaction)
        .filter(Transaction.category == None)  # noqa: E711
        .count()
    )
    return count


def get_most_recent_tran_date() -> datetime:
    db_conn = DatabaseAppSession()
    tran = db_conn.db_session.query(Transaction).order_by(Transaction.tran_date.desc()).limit(1).first()
    return tran.tran_date


def merchant_type_summary(year: str = '2022') -> List[List]:
    stmt = text('''
select period_month, merchant_type, count(merchant_type), sum(amount)*-1
from transaction
where period_year = :year and category = 'variable' and is_duplicate = false
group by period_month, merchant_type
order by period_month;
                ''')
    stmt = stmt.bindparams(year=year)
    db_conn = DatabaseAppSession()
    results = db_conn.db_engine.engine.execute(stmt).fetchall()
    typed_results = [['period_month', 'merchant_type', 'tran_count', 'total_amount']]
    for row in results:
        typed_results.append([row[0], row[1], row[2], float(row[3])])
    return typed_results


def get_tran_by_id(tran_id: str) -> Transaction:
    db_conn = DatabaseAppSession()
    tran = (
        db_conn.db_session.query(Transaction)
        .filter(Transaction.tran_id == tran_id)
        .first()
    )
    return tran

@dataclass
class BudgetTagGroups:
    budget_category: str
    budget_tag: str
    amount: float
    period: str

def get_transactions_grouped_by_budget_tag(year: str = '2022') -> List[BudgetTagGroups]:
    db_conn = DatabaseAppSession()
    raw_results = (
        db_conn.db_session
        .query(Transaction.budget_category, Transaction.budget_tag, func.sum(Transaction.amount), Transaction.period_month)
        .filter(Transaction.is_duplicate == False)  # noqa E712
        .filter(Transaction.period_year == year)
        .filter(Transaction.category != 'income')
        .filter(Transaction.category != 'transfer')
        .group_by(Transaction.budget_category, Transaction.budget_tag, Transaction.period_month)
        .order_by(Transaction.period_month)
        .all()
    )
    results = []
    for tran in raw_results:
        bg = BudgetTagGroups(tran[0], tran[1], tran[2], tran[3])
        if not bg.budget_category:
            bg.budget_category = 'unknown'
            bg.budget_tag = 'unknown'
        results.append(bg)
    return results


if __name__ == '__main__':
    budget_tags = get_transactions_grouped_by_budget_tag()
    pass
