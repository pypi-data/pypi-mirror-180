from typing import List
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import sessionmaker, Session, Query
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Date, JSON, NUMERIC, Boolean
import wdig.config as config
from wdig.parse import ParsedTransaction


_db_connection_string_no_db = f"postgresql://{config.db_username}:{config.db_password}@{config.db_hostname}:{config.db_hostport}"
_db_connection_string_with_db = _db_connection_string_no_db + f'/{config.db_dbname}'

_db_app_engine = None
_db_app_session = None


class DatabaseAppSession:
    """manages a database connection and session for the lifetime of the application"""

    @property
    def db_engine(self):
        global _db_app_engine
        if not _db_app_engine:
            _db_app_engine = create_engine(_db_connection_string_with_db, echo=False)
        return _db_app_engine

    @property
    def db_session(self) -> Session:
        global _db_app_session
        if not _db_app_session:
            session_maker = sessionmaker(bind=self.db_engine)
            _db_app_session = session_maker()
        return _db_app_session


def add_parsed_transaction(parsed_tran: ParsedTransaction) -> None:
    db_conn = DatabaseAppSession()
    tran = Transaction()

    tran.tran_id = parsed_tran.unique_id
    tran.tran_type = parsed_tran.tran_type
    tran.amount = parsed_tran.amount
    tran.tran_date = parsed_tran.tran_date
    tran.description = parsed_tran.description
    tran.account_number = parsed_tran.account_number
    tran.account_name = parsed_tran.account_name
    tran.bank_name = parsed_tran.bank_name
    tran.account_format = parsed_tran.account_format
    tran.original_columns = parsed_tran.original
    tran.imported_date = parsed_tran.imported_date
    tran.file_name = parsed_tran.file_name
    tran.is_duplicate = False

    db_conn.db_session.add(tran)


def commit_changes() -> None:
    db_conn = DatabaseAppSession()
    db_conn.db_session.commit()


def setup_database():
    engine = create_engine(
        _db_connection_string_no_db, echo=True, isolation_level="AUTOCOMMIT"
    )
    # https://docs.sqlalchemy.org/en/13/core/connections.html
    with engine.connect() as conn:
        try:
            conn.execute(f"CREATE DATABASE {config.db_dbname};")
        except ProgrammingError:
            pass

    engine = create_engine(
        _db_connection_string_with_db, echo=True, isolation_level="AUTOCOMMIT"
    )
    Base.metadata.create_all(engine)


Base = declarative_base()


class GoodBudgetTransaction(Base):
    __tablename__ = 'goodbudget_transaction'
    id = Column(Integer, primary_key=True)
    tran_date = Column(Date, nullable=True)
    envelope = Column(String(1000), nullable=True)
    details = Column(String(1000), nullable=True)
    name = Column(String(1000), nullable=True)
    check_num = Column(String(1000), nullable=True)
    notes = Column(String(1000), nullable=True)
    amount = Column(NUMERIC(12, 2), nullable=True)
    matched_tran_id = Column(UUID, nullable=True)


class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True)
    tran_id = Column(UUID, nullable=False)
    tran_type = Column(String(16), nullable=False)
    amount = Column(NUMERIC(12, 2), nullable=False)
    tran_date = Column(Date, nullable=False)
    description = Column(String(1000), nullable=False)
    account_number = Column(String(100), nullable=False)
    account_name = Column(String(100), nullable=False)
    bank_name = Column(String(100), nullable=False)
    account_format = Column(String(100), nullable=False)
    original_columns = Column(JSON, nullable=False)
    tag = Column(String(20))
    category = Column(String(40))
    imported_date = Column(DateTime, nullable=False)
    file_name = Column(String(100), nullable=False)
    is_duplicate = Column(Boolean, nullable=False)
    merchant_type = Column(String(100), nullable=True)
    period_year = Column(String(4), nullable=True)
    period_month = Column(String(6), nullable=True)
    budget_category = Column(String(40), nullable=True)
    budget_tag = Column(String(40), nullable=True)


class TransactionIterator(DatabaseAppSession):
    def __init__(self, batch_size=10, auto_commit=True, period_month=None, period_year=None) -> None:
        super().__init__()
        self.batch_size = batch_size
        self.auto_commit = auto_commit
        self.period_month = period_month
        self.period_year = period_year

    def __iter__(self):
        self.position = 0
        return self

    def _build_base_query(self) -> Query:

        if self.db_session.dirty:
            self.commit()

        query = self.db_session.query(Transaction)
        if self.period_month:
            query = (
                query
                .filter(Transaction.period_month == self.period_month)
                .filter(Transaction.period_year == self.period_year)
            )

        return query

    def __next__(self) -> List[Transaction]:
        if self.db_session.dirty:
            self.commit()

        query = self._build_base_query()

        results = self._build_base_query() \
            .order_by(Transaction.id) \
            .offset(self.position) \
            .limit(self.batch_size) \
            .all()

        # result = self.db_session.execute(stmt).scalars().all()
        if len(results) == 0:
            raise StopIteration
        self.position += self.batch_size
        return results

    @property
    def dirty(self) -> bool:
        return self.db_session.dirty

    def commit(self) -> None:
        self.db_session.commit()

    def rollback(self) -> None:
        self.db_session.rollback()

    @property
    def total_batches(self) -> int:
        count = self._build_base_query().count()
        return count / self.batch_size


if __name__ == "__main__":
    for batch in TransactionIterator():
        print('---')
        for tran in batch:
            tran.account_name = tran.account_name
            print(tran.id)
