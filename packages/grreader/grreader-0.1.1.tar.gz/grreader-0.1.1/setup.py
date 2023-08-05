# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['grreader']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'furl>=2.1.3,<3.0.0',
 'lxml>=4.9.1,<5.0.0',
 'pendulum>=2.1.2,<3.0.0',
 'requests-cache>=0.9.7,<0.10.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'grreader',
    'version': '0.1.1',
    'description': 'Python interface for the Goodreads API',
    'long_description': '### GR Reader\nThis is the grreader\n',
    'author': 'John N',
    'author_email': 'niedrachj@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
