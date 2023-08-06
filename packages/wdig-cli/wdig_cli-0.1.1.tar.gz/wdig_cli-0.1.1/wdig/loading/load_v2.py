from dataclasses import dataclass
import os
from typing import List
from rich.console import Console
from wdig.parse import ParsedTransaction, parse_row
import csv
from wdig.config import config
from wdig.database_v2 import Transaction, database_session
from datetime import datetime, timedelta
from sqlalchemy import func
from wdig.user_notifier import UserNotifier, NotificationMessage


console = Console()
notifier = UserNotifier()


@dataclass
class BankFileInfo():
    file_name: str
    transaction_count: int


class BankFileLoaderV2():
    def get_files(self):
        with database_session() as db:
            results = (
                db
                .query(Transaction.file_name, func.count(Transaction.file_name))
                .group_by(Transaction.file_name)
                .order_by(Transaction.file_name)
                .all()
            )
        # TODO map results to dataclass - nice way to do this?

    def get_date_for_new_files(self) -> datetime:
        with database_session() as db:
            tran = db.query(Transaction).order_by(Transaction.tran_date.desc()).limit(1).first()
            if tran:
                return tran.tran_type + timedelta(days=-2)
            else:
                return datetime.now() + timedelta(days=-90)

    def load_file(self, path_to_file: str, force: bool = False) -> int:
        """returns number of trans loaded"""
        filename = os.path.basename(path_to_file)
        # TODO if not already loaded, or force
        with open(path_to_file, 'r') as file:
            trans = []
            for row in csv.DictReader(file):
                parsed_tran = parse_row(row, filename)
                tran = self._to_transaction(parsed_tran)
                trans.append(tran)
            with database_session() as db:
                db.add_all(trans)
                db.commit()
        notifier.send(NotificationMessage(f'loaded {len(trans)} transactions from {filename}'))
        return len(trans)

    def load_new_files(self) -> List[str]:
        new_files = []
        for root, dirnames, filenames in os.walk(config.path_to_bank_files):
            for filename in filenames:
                if not filename.lower().endswith('.csv'):
                    continue
                # TODO check if file already loaded
                new_files.append(filename)
        notifier.send(NotificationMessage(f'found {len(new_files)} new bank files to load'))

        total_transactions = 0
        for filename in new_files:
            tran_count = self.load_file(os.path.join(root, filename))
            total_transactions += tran_count
        notifier.send(NotificationMessage(f'successfully loaded {total_transactions} transactions from {len(new_files)} new files'))

        return new_files

    def _to_transaction(self, parsed_tran: ParsedTransaction) -> Transaction:
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
        return tran


if __name__ == '__main__':
    bfl = BankFileLoaderV2()
    # new_files = bfl.load_new_files()
    bfl.get_files()
