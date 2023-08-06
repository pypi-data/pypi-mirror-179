# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['norske_kommuner']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'norske-kommuner',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Anders Steen',
    'author_email': 'anders.steen@knowit.no',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
