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
    'version': '2.0.1',
    'description': '',
    'long_description': '# Lingyin Bot\n\n## 启动机器人\n\n1.  `pip3 install poetry` 安装peorty包管理器和onebot适配器\n2.  `poetry install` 安装依赖\n3.  `poetry run python3 bot.py` 启动bot\n<!-- 3.  `source venv/bin/activate && python3 bot.py` 启动bot -->\n\n# 作为插件安装\n\nLingyin Bot中的源码已作为插件发布，如果觉得有帮助需要继承到自己的Bot中可以使用两种方法：\n\n1.  直接复制源码中的插件到自己的bot的plugin目录下，然后加上相应的配置即可\n2.  通过包管理器安装，可以通过nb，pip3，或者poetry等方式安装\n\n第一种可能需要一定的基础，第二种几行命令就可以搞定，但是方便自定义功能。\n\n## 多账户ChatGPT\n\n### 安装\n\n~~第一种方式~~（暂时不行，等待pr通过）\n\n```\nnb plugin install nonebot_plugin_multi_chatgpt\n```\n\n------\n\n第二种方式，使用一下命令安装\n\n```\npip3 install nonebot-plugin-multi-chatgpt==1.0.0\n```\n\n随后在`bot.py`中加上如下代码，加载插件\n\n```\nnonebot.load_plugin(\'nonebot_plugin_multi_chatgpt\')\n```\n\n### 配置\n\n在`.env.dev`中配置自己的`chatgpt_session_token_list`即可\n\n多个token，请注意不能换行只能写成一排 例如 \n\n```\nchatgpt_session_token_list = ["xxx", "yyy", "zzz"]\n```\n\n如果只有一个session也需要用数组的形式 \n\n```\nchatgpt_session_token_list = ["xxxx"]\n```\n\n获取token得方法，打开Application选项卡 > Cookie，复制值`__Secure-next-auth.session-token`并将其粘贴到在`.env.dev`中`session_token`即可。不需要管Authorization的值。\n![](https://chrisyy-images.oss-cn-chengdu.aliyuncs.com/img/image-20221205094326498.png)\n\n### Todo\n\n- [ ] 返回值渲染为图片\n- [ ] 完善密码登陆\n',
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
