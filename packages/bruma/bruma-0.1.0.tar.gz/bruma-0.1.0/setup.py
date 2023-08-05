# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bruma']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'bruma',
    'version': '0.1.0',
    'description': 'Bruma',
    'long_description': '',
    'author': 'José Antonio Perdiguero López',
    'author_email': 'perdy@perdy.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/perdy/bruma',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<3.12',
}


setup(**setup_kwargs)
