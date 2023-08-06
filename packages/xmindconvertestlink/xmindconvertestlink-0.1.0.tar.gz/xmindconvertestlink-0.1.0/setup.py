# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xmindconvertestlink']

package_data = \
{'': ['*']}

install_requires = \
['xmindparser==1.0.8']

setup_kwargs = {
    'name': 'xmindconvertestlink',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'qiangyanwen',
    'author_email': '508737091@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
