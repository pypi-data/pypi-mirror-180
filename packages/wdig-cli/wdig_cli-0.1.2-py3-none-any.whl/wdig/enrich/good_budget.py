"""
found this isn't easy to match -- probably dates wrong?
counts: {'matched': 51, 'duplicated': 1, 'nomatch': 138}


download goodbudget files (weekly?)
load function! -- use existing loadfunction -- need somewhere to store them (new table with forign key?).
try to match each to a transaction (new columns: goodbudget desc, goodbudget date, good budget envelope)
not matches goto unmatched spreadsheet worksheet

summary of variable by goodbuget envelope - can use transactions worksheet filtering?

TODO use a view for querying transactions - including linked GB trans

"""

from csv import DictReader
import datetime
from typing import Counter
from wdig.database import GoodBudgetTransaction, Transaction
from wdig.database import DatabaseAppSession


def load():
    gb_trans = []
    with open('data-in/goodbudget/history.csv', 'r') as f:
        for row in DictReader(f):
            gbt = GoodBudgetTransaction()
            gbt.tran_date = datetime.datetime.strptime(row['Date'], '%d/%m/%Y')
            gbt.amount = float(row['Amount'])
            gbt.check_num = row['Check #']
            gbt.details = row['Details']
            gbt.envelope = row['Envelope']
            gbt.name = row['Name']
            gbt.notes = row['Notes']
            gb_trans.append(gbt)

    db = DatabaseAppSession()
    db.db_session.query(GoodBudgetTransaction).delete()  # need to delete all and recreate - GB exports 1 file will all transactions
    db.db_session.add_all(gb_trans)
    db.db_session.commit()


def match():
    db = DatabaseAppSession()
    gb_trans = db.db_session.query(GoodBudgetTransaction).all()

    counts = {'matched': 0, 'duplicated': 0, 'nomatch': 0}
    for gb_tran in gb_trans:
        match_trans = db.db_session.query(Transaction) \
            .filter(Transaction.is_duplicate is False, Transaction.tran_date == gb_tran.tran_date.strftime('%Y-%m-%d'), Transaction.amount == gb_tran.amount) \
            .all()
        if len(match_trans) == 1:
            gb_tran.matched_tran_id = match_trans[0].tran_id
            db.db_session.commit()
            counts['matched'] += 1
        elif len(match_trans) > 1:
            counts['duplicated'] += 1
            # raise Exception('duplicate matches!')
        else:
            counts['nomatch'] += 1
    print(counts)


if __name__ == '__main__':
    load()
    match()
