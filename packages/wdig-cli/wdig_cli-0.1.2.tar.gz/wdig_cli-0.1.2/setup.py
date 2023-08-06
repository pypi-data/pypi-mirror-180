# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wdig', 'wdig.enrich', 'wdig.loading', 'wdig.outputs']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.27,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'numpy>=1.23.5,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'rich>=12.6.0,<13.0.0',
 'sqlalchemy>=1.4.44,<2.0.0',
 'tinydb>=4.7.0,<5.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['wdig = wdig.__main__:cli']}

setup_kwargs = {
    'name': 'wdig-cli',
    'version': '0.1.2',
    'description': 'Where Did It Go?',
    'long_description': '# wdig\n\n[![wdig](https://github.com/jebu4/wdig/actions/workflows/wdig.yml/badge.svg)](https://github.com/jebu4/wdig/actions/workflows/wdig.yml)\n\nwhere did it go?\n\n## tasks\n\n### dev ci\n\n```bash\nnox\n```\n',
    'author': 'Casey Burns',
    'author_email': 'CaseyBurns@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
