# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['csrspy']

package_data = \
{'': ['*']}

install_requires = \
['pyproj>=3.4.0,<4.0.0']

setup_kwargs = {
    'name': 'csrspy',
    'version': '0.4.0',
    'description': 'ITRF/NAD83CSRS coordinate transforms in Python',
    'long_description': 'None',
    'author': 'Taylor Denouden',
    'author_email': 'taylordenouden@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
