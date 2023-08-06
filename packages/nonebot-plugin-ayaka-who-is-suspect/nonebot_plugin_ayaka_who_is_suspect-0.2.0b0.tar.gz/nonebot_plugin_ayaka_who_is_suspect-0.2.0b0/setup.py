# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ayaka_who_is_suspect']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.1.3,<3.0.0',
 'nonebot-plugin-ayaka>=0.5.1b2,<0.6.0',
 'nonebot2>=2.0.0b5,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ayaka-who-is-suspect',
    'version': '0.2.0b0',
    'description': '谁是卧底',
    'long_description': '# 谁是卧底 0.2.0b0\n\n**注意：目前兼容性较差，如果有其他插件受到影响，请安装0.1.1版本**\n\n\n基于[ayaka](https://github.com/bridgeL/nonebot-plugin-ayaka)开发的 谁是卧底 小游戏\n\n任何问题欢迎issue\n\n## 安装插件\n\n`nb plugin install nonebot-plugin-ayaka-who-is-suspect`\n\n## 文档\n\nhttps://bridgel.github.io/ayaka_doc/latest/games/who-is-suspect/\n',
    'author': 'Su',
    'author_email': 'wxlxy316@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bridgeL/nonebot-plugin-ayaka-who-is-suspect',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
