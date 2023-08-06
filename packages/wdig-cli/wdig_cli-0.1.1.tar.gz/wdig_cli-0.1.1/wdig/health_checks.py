from optparse import check_choice
import os
from xml.dom import NotFoundErr
from rich.console import Console
from wdig.google_sheets import google_connect
from wdig.queries import get_transaction_count
import wdig.config as config


console = Console()


class HealthChecks:
    def check_health(self) -> None:
        health_checks = {}

        def check_data_in_folder_exists():
            if not os.path.exists(config.data_in_path):
                raise NotFoundErr()
        health_checks['check datafolder exists'] = check_data_in_folder_exists

        def check_db():
            get_transaction_count()
        health_checks['check database access'] = check_db

        def check_google_api():
            google_connect()
        health_checks['check google api access'] = check_google_api

        def check_data_file_count():
            file_count = 0
            for root, dirnames, filenames in os.walk(config.data_in_path):
                for filename in filenames:
                    if filename.lower().endswith('.csv'):
                        file_count += 1

            if file_count <= 0:
                raise NotFoundErr()
        health_checks['check data file count'] = check_data_file_count

        for key in health_checks.keys():
            console.print(f'[bold]{key}...', end='')
            try:
                health_checks[key]()
                console.print(f"[green] \u2713 PASSED")
            except Exception as ex:
                console.print(f"[red] \u2717 FAILED")
                console.print(f"[red]{ex}")


if __name__ == "__main__":  # pragma: no cover
    hc = HealthChecks()
    hc.check_health()
