# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gendiff', 'gendiff.formatter', 'gendiff.scripts']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'flake8>=5.0.4,<6.0.0',
 'pytest-cov>=4.0.0,<5.0.0',
 'pytest>=7.2.0,<8.0.0']

entry_points = \
{'console_scripts': ['gendiff = gendiff.scripts.gendiff:main']}

setup_kwargs = {
    'name': 'weii3hai-gendiff',
    'version': '0.1.1',
    'description': 'finds the difference between files',
    'long_description': '### Hexlet tests and linter status:\n[![Actions Status](https://github.com/WeibHai/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/WeibHai/python-project-50/actions)\n\n<a href="https://codeclimate.com/github/WeibHai/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/0879bbf43057d1a6bbc1/maintainability" /></a>\n\n<a href="https://codeclimate.com/github/WeibHai/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/0879bbf43057d1a6bbc1/test_coverage" /></a>\n\nComparison of deep nested files formatter mode - stylish (JSON and YML) - asciinema https://asciinema.org/a/I4SYMHBrQ6HbzhbMwZSCw82Ed\n\nComparison of deep nested files formatter mode - plain (JSON and YML) - asciinema https://asciinema.org/a/KFm70M6D6LrZq4V2tWBmMwTiM\n\nFlat JSON file comparison - asciinema https://asciinema.org/a/KXMf4zAZtkXZcyGCEXKNfbTA4\n\nFlat YML file comparison - asciinema https://asciinema.org/a/BnpoQyXUH3P0Tw3UsiiDXQYMe',
    'author': 'weii3hai',
    'author_email': 'weii3hai@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
