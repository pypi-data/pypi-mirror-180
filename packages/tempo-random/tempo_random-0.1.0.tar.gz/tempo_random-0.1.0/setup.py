# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tempo_random']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['tempo = tempo_random.main:app']}

setup_kwargs = {
    'name': 'tempo-random',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Simple Typer CLI\n\n[<img src="img/interrogate_badge.svg">]() [![Python application](https://github.com/mrcartoonster/cli_rando/actions/workflows/first_action.yml/badge.svg?branch=main)](https://github.com/mrcartoonster/cli_rando/actions/workflows/first_action.yml)\n\nSimple CLI to practice with typer and Github actions.\n',
    'author': 'evan',
    'author_email': 'evan@pop-os.localdomain',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
