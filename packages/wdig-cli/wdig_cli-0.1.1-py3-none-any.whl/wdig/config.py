"""
using TOML for config files https://toml.io/en/
"""

import os
import os.path as path
import toml
import json


class Config():
    _values = {}

    def __init__(self) -> None:
        self._path_to_config_file = path.expanduser('~/.wdig/config.toml')
        self.load()

    def _set_default_values(self):
        self._values = {}
        self._values['path_to_sqlite_db'] = '~/.wdig/wdig.sqlite.db'
        self._values['path_to_bank_files'] = ''

    def load(self):
        if not path.exists(self.path_to_config_file):
            self.reset_to_default()

        with open(self.path_to_config_file, 'r') as file:
            self._values = toml.load(file)

    def save(self):
        os.makedirs(path.dirname(self.path_to_config_file), exist_ok=True)
        with open(self.path_to_config_file, 'w+') as file:
            toml.dump(self._values, file)

    def reset_to_default(self) -> None:
        if path.exists(self.path_to_config_file):
            os.remove(self.path_to_config_file)
        self._set_default_values()
        self.save()

    def to_toml(self) -> str:
        return toml.dumps(self._values)

    def to_json(self) -> str:
        return json.dumps(self._values)

    def to_dict(self) -> dict:
        return dict.copy(self._values)

    @property
    def path_to_config_file(self) -> str:
        return self._path_to_config_file

    @property
    def path_to_sqlite_db(self) -> str:
        return path.expanduser(self._values['path_to_sqlite_db'])

    @property
    def path_to_bank_files(self) -> str:
        return path.expanduser(self._values['path_to_bank_files'])

    @path_to_bank_files.setter
    def path_to_bank_files(self, value: str):
        self._values['path_to_bank_files'] = value
        self.save()


config = Config()

if __name__ == '__main__':
    config.reset_to_default()
    print(config.path_to_config_file)


development = ('WDIG-LIVE' not in os.environ.keys())

app_name = "wdig"
if development:
    app_name += '-dev'

version = 'x.y.z'  # how to get this from docker tags?


# google
google_auth_filepath = '.secrets/google-auth.json'
google_wdig_folder_id = "1XjS2bvm56rwv0D3KwaUAAmy3E5QCY0kZ"


# data
data_in_path = 'data-in'


# database
db_username = 'postgres'
db_password = os.environ.get('WDIG_DB_PASSWORD')
db_hostname = os.environ.get('WDIG_DB_HOST', 'localhost')
db_hostport = '5432'
# pick db name based on config.development
db_dbname = 'wdig_dev'
if not development:
    db_dbname = 'wdig'
