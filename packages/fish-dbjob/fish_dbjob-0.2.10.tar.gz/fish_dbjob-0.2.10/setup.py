# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fish_dbjob', 'fish_dbjob.services']

package_data = \
{'': ['*']}

install_requires = \
['databricks-cli>=0.17.0,<0.18.0',
 'tabulate>=0.9.0,<0.10.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['fish-dbjob = fish_dbjob.cli:app']}

setup_kwargs = {
    'name': 'fish-dbjob',
    'version': '0.2.10',
    'description': '',
    'long_description': '# Databricks job permission \n\nDatabricks job permission cli',
    'author': 'Tim Chen',
    'author_email': 'firstim@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
