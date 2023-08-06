# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['experiment']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1,<8.0']

entry_points = \
{'console_scripts': ['experiment = experiment.__main__:main']}

setup_kwargs = {
    'name': 'experiment-drone',
    'version': '0.1.4',
    'description': 'Python Boilerplate contains all the boilerplate you need to create a Python package.',
    'long_description': 'None',
    'author': 'bopo',
    'author_email': 'ibopo@126.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
