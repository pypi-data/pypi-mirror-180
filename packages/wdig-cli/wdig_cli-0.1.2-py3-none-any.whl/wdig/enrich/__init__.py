from wdig.database import TransactionIterator
from wdig.enrich.categories import apply_category
from wdig.enrich.periods import apply_period
from rich.console import Console
from rich.progress import track
from wdig.queries import get_unenriched_transaction_count, get_transaction_count
from wdig.enrich.clean_data import dedup
from wdig.enrich.adjustments import apply_adjustments
from wdig.enrich.merchant_type import determine_merchant_type


console = Console()


def enrich_all_transactions():
    tran_count = get_transaction_count()
    unenriched_count = get_unenriched_transaction_count()
    console.print(f'found {tran_count} transactions, {unenriched_count} missing enrichment')

    iterator = TransactionIterator(period_month='10-Oct', period_year='2022')
    for trans in track(iterator, total=iterator.total_batches, description='Enriching transactions...'):
        for tran in trans:
            apply_period(tran)
            apply_category(tran)
            tran.merchant_type = determine_merchant_type(tran.description)
    apply_adjustments()
    dedup()
