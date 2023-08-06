# from wdig.health_checks import HealthChecks
# from wdig.load import BankFileLoader
import click
from rich.console import Console
# from wdig.queries import query_by_period, get_most_recent_tran_date, get_tran_by_id, get_transactions_grouped_by_budget_tag
from rich.table import Table
from wdig.config import config
# from wdig.google_sheets import update_empty_sheet, update_transaction_sheet
# from wdig.database import setup_database
# from wdig.enrich import enrich_all_transactions
# from datetime import timedelta, datetime
# from wdig.object_storage import BankFileObjectStorage
from rich import inspect
import logging
import pathlib
from wdig.cli_config import cli_config
from wdig.cli_files import cli_files
from wdig.user_notifier import NotificationMessage, UserNotifier


log_path = f'{pathlib.Path(__file__).parent.resolve()}/wdig.log'
logging.basicConfig(filename=log_path,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logging.info('wdig starting up!')


console = Console()


def handle_user_notification(msg: NotificationMessage) -> None:
    console.print(f'{msg.message}')


notifier = UserNotifier()
notifier.subscribe(handle_user_notification)


@click.group(help=f"Where Did It Go? (wdig)")
@click.version_option()
def cli():
    pass


cli.add_command(cli_config)
cli.add_command(cli_files)
if __name__ == "__main__":
    cli()


# @click.command(help="runs health checks and tests")
# def health():
#     health_check = HealthChecks()
#     health_check.check_health()

# # todo #52 re-enrich tran command
# # wdig enrich -> enrich if missing enrichment
# # wdig enrich --all -> enrich all
# # wdig enrich --tran-id xyz -> re-enrich tran
# # wdig enrich --update -> update too?

# @click.command(help="loads new data files")
# def load():
#     bfl = BankFileLoader()
#     count = bfl.load_new_files()

#     if count == 0:
#         last_tran_date = get_most_recent_tran_date()
#         last_tran_date += timedelta(days=-2)
#         console.print(f'go and download files from "{last_tran_date.strftime("%-d %b %y")}" to today')
#         console.print('these accounts; Kiwibank (cash, savings, onlinebills) bnz (revolving, cash, fixed) anz (cash, creditcard)')
#         console.print(f'put them in a folder named {datetime.now().strftime("%Y-%m-%d")}')


# @click.command(help="Count and Amount summary by period")
# @click.option('-m', '--months-back', type=int, default=6, required=True)
# def period(months_back: int, out_data_path: str):
#     df = query_by_period(out_data_path, months_back)
#     table = Table(show_header=True, header_style="bold magenta")
#     table.add_column("period_month", style="dim", width=12)
#     table.add_column("period_year", style="dim", width=12)
#     table.add_column("count", style="dim", width=12)
#     table.add_column("amount", style="dim", width=12)
#     for row in df.values:
#         table.add_row(str(row[0]), row[1], str(row[2]), str(row[3]))
#     console.print(table)


# @click.command(help='update google sheets')
# @click.option('-y', '--year', type=str, default=2022, required=True)
# def update(year):
#     with console.status(f"[bold]Updating empty test sheet...") as status:
#         update_empty_sheet()
#         console.print('Empty test sheet updated')

#     with console.status(f"[bold]Updating transation {year} year sheet...") as status:
#         update_transaction_sheet(year)
#         console.print(f'Transation {year} year sheet updated')


# @click.command(help='creates db and schema')
# def setupdb():
#     setup_database()


# @click.command(help='enrich all transactions')
# def enrich():
#     enrich_all_transactions()

# @click.command(help='Show info about a transaction')
# @click.option('-t', '--tran_id', type=str, required=True)
# def tran(tran_id):
#     tran = get_tran_by_id(tran_id)
#     inspect(tran, methods=False)


# @click.command(name='list')
# def files_list():
#     os = BankFileObjectStorage()
#     files = os.list_files()
#     for file in files:
#         console.print(file)


# @click.command(name='budget')
# def budget():
#     budget_tags = get_transactions_grouped_by_budget_tag()

#     current_period = ''
#     for bt in budget_tags:
#         if current_period != bt.period:
#             console.print('---')
#             current_period = bt.period
#         console.print(f'{bt.period} {bt.budget_tag} {bt.amount}')

# files.add_command(files_list)
# cli.add_command(health)
# cli.add_command(load)
# cli.add_command(period)
# cli.add_command(update)
# cli.add_command(setupdb)
# cli.add_command(enrich)
# cli.add_command(tran)
# cli.add_command(budget)
