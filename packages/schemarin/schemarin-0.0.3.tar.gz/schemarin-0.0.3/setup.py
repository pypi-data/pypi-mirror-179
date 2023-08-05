# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['schemarin']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'colorama>=0.4.6,<0.5.0',
 'colour>=0.1.5,<0.2.0',
 'halo>=0.0.31,<0.0.32',
 'inflect>=6.0.2,<7.0.0',
 'inquirerpy>=0.3.4,<0.4.0',
 'loctocat>=1.0.2,<2.0.0',
 'path>=16.5.0,<17.0.0',
 'pygit2>=1.11.1,<2.0.0',
 'pygithub>=1.57,<2.0',
 'pyperclip>=1.8.2,<2.0.0',
 'toml>=0.10.2,<0.11.0',
 'validators>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['schemarin = schemarin.schemarin:cli']}

setup_kwargs = {
    'name': 'schemarin',
    'version': '0.0.3',
    'description': 'A color scheme manager for iTerm2',
    'long_description': 'None',
    'author': 'celsius narhwal',
    'author_email': 'hello@celsiusnarhwal.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://schemarin.celsiusnarhwal.dev',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
