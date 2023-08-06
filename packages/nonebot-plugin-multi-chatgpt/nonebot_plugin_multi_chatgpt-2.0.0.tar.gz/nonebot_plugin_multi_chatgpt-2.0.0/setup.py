# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_multi_chatgpt']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.1.5,<3.0.0',
 'nonebot-plugin-apscheduler>=0.2.0,<0.3.0',
 'nonebot2>=2.0.0rc2,<3.0.0',
 'revchatgpt>=0.0.38.1,<0.0.39.0']

setup_kwargs = {
    'name': 'nonebot-plugin-multi-chatgpt',
    'version': '2.0.0',
    'description': '',
    'long_description': 'None',
    'author': 'chrisyy',
    'author_email': '1017975501@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
