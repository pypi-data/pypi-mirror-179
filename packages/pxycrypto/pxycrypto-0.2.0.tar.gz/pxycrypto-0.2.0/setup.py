# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pxycrypto']

package_data = \
{'': ['*'], 'pxycrypto': ['assets/*']}

setup_kwargs = {
    'name': 'pxycrypto',
    'version': '0.2.0',
    'description': '',
    'long_description': 'None',
    'author': 'Z1R343L',
    'author_email': 'jan2705g@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
