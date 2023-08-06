import click
from datetime import timedelta, datetime
from wdig.loading import BankFileLoaderV2
from rich.console import Console


console = Console()


@click.group('files')
def cli_files():
    pass

@click.command()
def list():
    pass

@click.command()
def new():
    bfl = BankFileLoaderV2()
    new_files = bfl.load_new_files()

    if len(new_files) == 0:
        last_tran_date = bfl.get_date_for_new_files()
        console.print(f'go and download files from "{last_tran_date.strftime("%-d %b %y")}" to today')
        console.print('these accounts; Kiwibank (cash, savings, onlinebills) bnz (revolving, cash, fixed) anz (cash, creditcard)')
        console.print(f'put them in a folder named {datetime.now().strftime("%Y-%m-%d")}')


cli_files.add_command(list)
cli_files.add_command(new)
