# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jmx2yaml']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML==5.3.1', 'lxml==4.6.2', 'simplejson==3.16.0']

setup_kwargs = {
    'name': 'jmx2yaml',
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
