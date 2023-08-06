from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Date, JSON, NUMERIC, Boolean
from wdig.config import config
from decimal import Decimal as D
import sqlalchemy.types as types


_engine = create_engine(f"sqlite:///{config.path_to_sqlite_db}")
_session_maker = sessionmaker(bind=_engine)

def database_session():
    return _session_maker()


class SqliteNumeric(types.TypeDecorator):
    impl = types.String

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(types.VARCHAR(100))

    def process_bind_param(self, value, dialect):
        return str(value)

    def process_result_value(self, value, dialect):
        return D(value)


Base = declarative_base()


class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True)
    tran_id = Column(String(16), nullable=False)
    tran_type = Column(String(16), nullable=False)
    amount = Column(SqliteNumeric(12, 2), nullable=False)
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
    period_year = Column(String(4), nullable=True)
    period_month = Column(String(6), nullable=True)
    budget_category = Column(String(40), nullable=True)
    budget_tag = Column(String(40), nullable=True)


def create_schema() -> None:
    Base.metadata.create_all(_engine)


def destroy_database() -> None:
    Base.metadata.delete_all()


if __name__ == '__main__':
    create_schema()
    with database_session() as db:
        pass
