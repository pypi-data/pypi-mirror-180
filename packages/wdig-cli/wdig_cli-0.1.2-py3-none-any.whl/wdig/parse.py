from dataclasses import dataclass
from datetime import datetime
import hashlib, re
from typing import Pattern


@dataclass(init=False)
class ParsedTransaction():
    # class with structure and validation!
    # transaction datamodel!!!!
    # create from dict + validation?

    def __init__(
        self,
        original: str,
        file_name: str
    ) -> None:
        self.original = original
        self.file_name = file_name
        self.imported_date = datetime.now().date()

    def to_dict(self):
        vars(self)

    unique_id: str
    tran_type: str  # credit or credit
    amount: float
    tran_date: datetime
    description: str
    account_number: str
    account_name: str
    bank_name: str
    account_format: str
    original: dict
    imported_date: datetime
    file_name: str


@dataclass
class BankAccount():
    account_name: str
    account_number: str
    bank_name: str
    account_file_format: str
    file_name_match_regex: Pattern

    def is_match(this, file_name: str) -> bool:
        return bool(re.search(this.file_name_match_regex, file_name))

    def parse_row(this, row, file_name: str) -> ParsedTransaction:
        tran = ParsedTransaction(
            file_name=file_name,
            original=row
        )
        tran.account_format = this.account_file_format
        tran.account_name = this.account_name
        tran.account_number = this.account_number
        tran.bank_name = this.bank_name
        if this.account_file_format == 'bnz-csv':
            this._parse_row_bnz(row, tran)
        elif this.account_file_format == 'kiwibank-csv':
            this._parse_row_kiwibank_cash(row, tran)
        elif this.account_file_format == 'anz-cc-csv':
            this._parse_row_anz_creditcard(row, tran)
        elif this.account_file_format == 'anz-csv':
            this._parse_row_anz_cash(row, tran)
        else:
            raise LookupError(f'Unknown bank file format {this.account_file_format}')
        return tran

    def _parse_row_bnz(this, row, tran: ParsedTransaction) -> None:
        tran.unique_id = hashlib.md5(bytes(f"{row['Payee']}-{row['Particulars']}-{row['Amount']}-{row['Date']}", encoding="utf-8",)).hexdigest()
        tran.description = f"{row['Payee']} {row['Particulars']}"
        tran.amount = float(row["Amount"])
        tran.tran_date = datetime.strptime(row["Date"], "%d/%m/%y").date()
        tran.tran_type = "debit"

    def _parse_row_kiwibank_cash(this, row, tran) -> ParsedTransaction:
        tran.unique_id = hashlib.md5(bytes(f"{row['Memo/Description']}-{row['Amount']}-{row['Date']}", encoding="utf-8")).hexdigest()
        tran.description = row["Memo/Description"]
        tran.amount = float(row["Amount"])
        tran.tran_date = datetime.strptime(row["Date"], "%d-%m-%Y")
        tran.type = "debit"
        if row["Amount (credit)"] is not None:
            tran.tran_type = "credit"

    def _parse_row_anz_creditcard(this, row, tran: ParsedTransaction) -> None:
        tran.unique_id = hashlib.md5(bytes(f"{row['Type']}-{row['Amount']}-{row['TransactionDate']}", encoding="utf-8", )).hexdigest()
        tran.description = row["Details"]
        tran.tran_date = datetime.strptime(row["TransactionDate"], "%d/%m/%Y")
        tran.amount = float(row["Amount"])
        tran.tran_type = "debit"
        if row["Type"] == "C":
            tran.tran_type = "credit"
        if tran.tran_type == "debit":
            tran.amount = tran.amount * -1

    def _parse_row_anz_cash(this, row, tran: ParsedTransaction) -> None:
        tran.unique_id = hashlib.md5(bytes(f"{row['Type']}-{row['Amount']}-{row['Date']}", encoding="utf-8",)).hexdigest()
        tran.description = f"{row['Details']} {row['Particulars']} {row['Code']}"
        tran.amount = float(row["Amount"])
        tran.tran_date = datetime.strptime(row["Date"], "%d/%m/%Y")
        tran.tran_type = "debit"
        if tran.amount < 0:
            tran.tran_type = "credit"


class BankAccountLookup():
    bank_accounts = [
        BankAccount('BNZ Cash', '02-1265-0038877-001', 'BNZ', 'bnz-csv', r'^Cash-'),
        BankAccount('BNZ Fixed Expenses', '02-1265-0038877-000', 'BNZ', 'bnz-csv', r'^Fixed-Expenses-'),
        BankAccount('BNZ Revolving Mortgage', '02-1265-0038877-083', 'BNZ', 'bnz-csv', r'^Revolving-Mortgage-'),
        BankAccount('Kiwibank Online Bills', '38-9010-0821604-08', 'Kiwibank', 'kiwibank-csv', r'38-9010-0821604-08'),
        BankAccount('Kiwibank Savings', '38-9010-0821604-16', 'Kiwibank', 'kiwibank-csv', r'38-9010-0821604-16'),
        BankAccount('Kiwibank Cash', '38-9010-0821604-09', 'Kiwibank', 'kiwibank-csv', r'38-9010-0821604-09'),
        BankAccount('ANZ Visa Gold', '4367-xxxx-xxxx-7631', 'ANZ', 'anz-cc-csv', r'4367-xxxx-xxxx-7631'),
        BankAccount('ANZ Cash', '06-0229-0443344-00', 'ANZ', 'anz-csv', r'06-0229-0443344-00'),
    ]

    def find_from_file_name(this, file_name: str) -> BankAccount:
        matches = [account for account in this. bank_accounts if account.is_match(file_name)]
        if len(matches) == 0:
            raise LookupError(f'unknown bank account for file {file_name}')
        elif len(matches) > 1:
            raise LookupError(f'file {file_name} has {len(matches)} matched bank accounts')
        return matches[0]


# TODO #51 why is this failing when built in container? param: row: dict[str, any]
def parse_row(row, file_name: str) -> ParsedTransaction:
    account_lookup = BankAccountLookup()
    account = account_lookup.find_from_file_name(file_name)
    return account.parse_row(row, file_name)
