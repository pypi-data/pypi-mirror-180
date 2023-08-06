import os
from rich.console import Console
from wdig.parse import parse_row
import csv
from wdig.database import add_parsed_transaction, commit_changes
from wdig.queries import is_file_already_loaded
import wdig.config as config
from wdig.object_storage import BankFileObjectStorage


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
        return is_file_already_loaded(filename)

    def _add_parsed_transaction(self, tran):
        add_parsed_transaction(tran)

    def _commit_changes(self):
        commit_changes()


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
    bfl = BankFileLoader()
    bfl.load_new_files()
