import click
from wdig.config import config
from rich.console import Console
from rich.prompt import Prompt
from wdig.database_v2 import create_schema


console = Console()


@click.group('config')
def cli_config():
    pass

@click.command()
def check():
    config_values = config.to_dict()
    console.print(f'read config file [bold green]\u2713')

@click.command()
def show():
    console.print(f'config stored in: {config.path_to_config_file}')
    console.print(config.to_toml())

@click.command()
def reset():
    config.reset_to_default()

@click.command()
def setup():
    bank_file_path = Prompt.ask("Enter path to bank files", default=config.path_to_bank_files)

    config.path_to_bank_files = bank_file_path
    console.print(f'update config [bold green]\u2713')

    create_schema()
    console.print(f'create db schema [bold green]\u2713')


cli_config.add_command(check)
cli_config.add_command(show)
cli_config.add_command(reset)
cli_config.add_command(setup)
