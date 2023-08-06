# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dj_image_finder']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'climage>=0.1.3,<0.2.0',
 'getkey>=0.6.5,<0.7.0',
 'google-search-results>=2.4.1,<3.0.0',
 'keyboard>=0.13.5,<0.14.0']

entry_points = \
{'console_scripts': ['djsearch = dj_image_finder.__init__:image']}

setup_kwargs = {
    'name': 'dj-image-finder',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'dongjin2008',
    'author_email': 'dkim@icsparis.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
