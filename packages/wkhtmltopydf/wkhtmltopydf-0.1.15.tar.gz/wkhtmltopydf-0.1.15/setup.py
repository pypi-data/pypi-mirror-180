# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wkhtmltopydf']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'wkhtmltopydf',
    'version': '0.1.15',
    'description': '',
    'long_description': '',
    'author': 'abonur',
    'author_email': 'sm7.abonur@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
