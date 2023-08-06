import os
from typing import List
from rich.console import Console
from wdig.parse import ParsedTransaction, parse_row
import csv
from wdig.database import add_parsed_transaction, commit_changes
from wdig.queries import is_file_already_loaded
import wdig.config as config
from wdig.loading.object_storage import BankFileObjectStorage
from wdig.database_v2 import Transaction, database_session


console = Console()


class BankFileLoader():

    def load_new_files(self) -> int:

        file_loaded_count = 0
        for root, dirnames, filenames in os.walk(config.data_in_path):
            for filename in filenames:
                if not filename.lower().endswith('.csv'):
                    continue

                in_filepath = os.path.join(root, filename)
                if self._is_file_already_loaded(filename):
                    continue

                self._save_object(filename, in_filepath)

                with open(in_filepath, 'r') as infile:
                    trans = []
                    for row in csv.DictReader(infile):
                        tran = parse_row(row, filename)
                        self._add_parsed_transaction(tran)
                        trans.append(tran)
                self._commit_changes()
                file_loaded_count += 1
                console.print(f'loaded {len(trans)} in {os.path.basename(in_filepath)}')

        console.print(f'[bold green] found {file_loaded_count} new files')
        return file_loaded_count

    def _save_object(self, filename: str, path_to_file: str) -> None:
        object_storage = BankFileObjectStorage()
        object_storage.save_file(key=filename, path_to_file=path_to_file)

    def _is_file_already_loaded(self, filename):
        # query it here?
        return False


class BankFileLoaderV2():
    def get_files():
        # transactions by file_name, count(),
        pass

    def load_file(self, path_to_file: str, force: bool = False) -> False:  # return load status?
        filename = os.path.basename(path_to_file)
        with open(path_to_file, 'r') as file:
            trans = []
            for row in csv.DictReader(file):
                parsed_tran = parse_row(row, filename)
                tran = self._to_transaction(parsed_tran)
                trans.append(tran)
            with database_session() as db:
                db.add_all(trans)
                db.commit()

    def load_new_files(self) -> List[str]:
        new_files = []
        for root, dirnames, filenames in os.walk(config.data_in_path):
            for filename in filenames:
                if not filename.lower().endswith('.csv'):
                    continue

                # TODO if not already loaded
                self.load_file()

                new_files.append(filename)

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


# TODO the abstraction (resource access) should be testable!
class BankFileLoaderTestable(BankFileLoader):
    def __init__(self, is_file_already_loaded: bool) -> None:
        super().__init__()
        self.is_file_already_loaded = is_file_already_loaded

    def _is_file_already_loaded(self, filename):
        return self.is_file_already_loaded

    def _save_object(self, filename: str, path_to_file: str) -> None:
        pass

    def _add_parsed_transaction(self, tran):
        pass

    def _commit_changes(self):
        pass


if __name__ == '__main__':
    bfl = BankFileLoaderV2
    bfl.load_new_files()
