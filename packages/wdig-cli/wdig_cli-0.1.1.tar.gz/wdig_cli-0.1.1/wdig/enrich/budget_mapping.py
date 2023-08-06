from wdig.database import TransactionIterator, Transaction
from wdig.enrich.budget_mapping_debt import map_to_debt_budget
from wdig.enrich.budget_mapping_fixed import map_to_fixed_budget
from wdig.enrich.budget_mapping_variable import map_to_variable_budget
from wdig.enrich.budget_mapping_mortgage import map_to_mortgage_budget
from wdig.enrich.budget_mapping_savings import map_to_savings_budget
from wdig.enrich.budget_mapping_donations import map_to_donations_budget
from wdig.enrich.budget_mapping_income import map_to_income_budget
from wdig.enrich.budget_mapping_transfer import map_to_transfer_budget
from rich.progress import track
import logging


def map_to_budget(tran: Transaction):
    if map_to_fixed_budget(tran):
        return
    if map_to_debt_budget(tran):
        return
    if map_to_variable_budget(tran):
        return
    if map_to_mortgage_budget(tran):
        return
    if map_to_savings_budget(tran):
        return
    if map_to_donations_budget(tran):
        return
    if map_to_income_budget(tran):
        return
    if map_to_transfer_budget(tran):
        return


# TODO make this multi-threaded
if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    logging.info('hi!')

    period_month = '10-Oct'
    period_year = '2022'

    interator = TransactionIterator(period_month=period_month, period_year=period_year)
    for batch in track(interator, total=interator.total_batches, description='budget mapping transactions...'):
        for tran in batch:
            map_to_budget(tran)
