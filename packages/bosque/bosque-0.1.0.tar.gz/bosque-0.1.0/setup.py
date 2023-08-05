# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bosque']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'bosque',
    'version': '0.1.0',
    'description': 'Bosque',
    'long_description': '',
    'author': 'José Antonio Perdiguero López',
    'author_email': 'perdy@perdy.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/perdy/bosque',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<3.12',
}


setup(**setup_kwargs)
