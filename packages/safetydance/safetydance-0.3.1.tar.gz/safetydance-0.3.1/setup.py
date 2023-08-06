# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['safetydance']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'safetydance',
    'version': '0.3.1',
    'description': 'A typesafe system for defining and composing steps.',
    'long_description': None,
    'author': 'David Charboneau',
    'author_email': 'david@adadabase.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dcharbon/safetydance',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
