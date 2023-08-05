# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fmover']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0', 'notifypy>=1.0.3.0,<2.0.0.0']

entry_points = \
{'console_scripts': ['fmover = fmover.__main__:main']}

setup_kwargs = {
    'name': 'fmover',
    'version': '0.0.4',
    'description': 'Move files based on file properties and given criteria',
    'long_description': 'None',
    'author': 'Ephraim Siegfried',
    'author_email': 'ephraim.siegfried@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/EphraimSiegfried/fmover',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
