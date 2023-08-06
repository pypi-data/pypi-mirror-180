# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pylithiumsso3']

package_data = \
{'': ['*']}

install_requires = \
['pycryptodome>=3.15.0,<4.0.0']

setup_kwargs = {
    'name': 'pylithiumsso3',
    'version': '0.1.1',
    'description': 'Python 3 port of lithium_sso.php',
    'long_description': '# pylithiumsso3\n\nPython 3 port of lithium_sso.php\n\n## Installation\n\nTo install `pylithiumsso3` and its dependencies, run this:\n\n    pip install pylithiumsso3\n    \nThis package requires python 3.8 or better.\n\n## API\n\nSee [this page](https://rzuckerm.github.io/pylithiumsso3) for details.\n',
    'author': 'Ron Zuckerman',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rzuckerm/pylithiumsso3',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
