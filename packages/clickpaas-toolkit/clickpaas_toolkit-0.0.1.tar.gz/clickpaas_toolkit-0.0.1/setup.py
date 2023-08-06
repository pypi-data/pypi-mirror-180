# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clickpaas_toolkit',
 'clickpaas_toolkit.conn',
 'clickpaas_toolkit.datastore',
 'clickpaas_toolkit.http',
 'clickpaas_toolkit.log',
 'clickpaas_toolkit.utils']

package_data = \
{'': ['*']}

install_requires = \
['pycryptodomex==3.12.0',
 'pymongo==3.6.1',
 'pymysql==0.9.1',
 'python-json-logger==0.1.9',
 'redis==2.10.6',
 'requests==2.22.0',
 'simplejson==3.16.0']

setup_kwargs = {
    'name': 'clickpaas-toolkit',
    'version': '0.0.1',
    'description': 'Toolkit for clickpaas api test framework',
    'long_description': None,
    'author': 'qiangyanwen',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
