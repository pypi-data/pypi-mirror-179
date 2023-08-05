# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vscode_server_bin']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'vscode-server-bin',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'ZhengYu, Xu',
    'author_email': 'zen-xu@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
