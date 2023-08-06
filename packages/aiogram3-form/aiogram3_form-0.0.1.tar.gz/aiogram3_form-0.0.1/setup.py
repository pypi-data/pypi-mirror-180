# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiogram3_form']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aiogram3-form',
    'version': '0.0.1',
    'description': 'A library to create forms in aiogram3',
    'long_description': '# aiogram3-form\nA library to create forms in aiogram3\n',
    'author': 'TrixiS',
    'author_email': 'oficialmorozov@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
