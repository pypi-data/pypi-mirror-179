# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['witchtui']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['witchtui = witchtui:run']}

setup_kwargs = {
    'name': 'witchtui',
    'version': '0.1.1',
    'description': 'A Immediate Command line User Interface for Python',
    'long_description': None,
    'author': 'François Poizat',
    'author_email': 'francois.poizat@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
