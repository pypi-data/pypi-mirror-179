# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dockyard_cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['dcli = dockyard_cli.main:main']}

setup_kwargs = {
    'name': 'dockyard-cli',
    'version': '0.1.3',
    'description': 'CLI for dockyard',
    'long_description': 'Usage\n======\n\n1. Configure dockyard cli using `dcli configure`\n2. Connect to dockyard workspace using `dcli ssh <workspace name>`\n\n',
    'author': 'rsingh',
    'author_email': 'rsingh@altoslabs.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
