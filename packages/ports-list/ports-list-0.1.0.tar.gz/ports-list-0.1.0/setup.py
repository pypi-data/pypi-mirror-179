# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ports_list']

package_data = \
{'': ['*']}

install_requires = \
['psutil>=5.9.4,<6.0.0', 'textual>=0.5.0,<0.6.0']

setup_kwargs = {
    'name': 'ports-list',
    'version': '0.1.0',
    'description': 'List listening ports on terminal',
    'long_description': None,
    'author': 'lethe',
    'author_email': 'lethe30003000@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
