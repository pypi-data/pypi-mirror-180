# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shipbob', 'shipbob.models']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'shipbob',
    'version': '0.2.0',
    'description': 'Client SDK for ShipBob API',
    'long_description': 'None',
    'author': 'Raphael Lullis',
    'author_email': 'raphael@communityphone.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
