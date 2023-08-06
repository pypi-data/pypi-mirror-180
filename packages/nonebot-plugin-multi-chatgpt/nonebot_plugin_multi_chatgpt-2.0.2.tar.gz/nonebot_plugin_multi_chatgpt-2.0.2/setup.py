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
 'revchatgpt>=0.0.38.7,<0.0.39.0']

setup_kwargs = {
    'name': 'nonebot-plugin-multi-chatgpt',
    'version': '2.0.2',
    'description': '',
    'long_description': '# 多账户ChatGPT\n\n\n\n## 安装\n\n~~第一种方式~~（暂时不行，等待pr通过）\n\n```\nnb plugin install nonebot_plugin_multi_chatgpt\n```\n\n------\n\n第二种方式，使用一下命令安装\n\n```\npip3 install nonebot_plugin_multi_chatgpt --upgrade\n```\n\n随后在`bot.py`中加上如下代码，加载插件\n\n```\nnonebot.load_plugin(\'nonebot_plugin_multi_chatgpt\')\n```\n\n## 配置\n\n### token方式\n\n在`.env.dev`中配置自己的`chatgpt_session_token_list`即可\n\n多个token，请注意不能换行只能写成一排 例如 \n\n```\nchatgpt_session_token_list = ["xxx", "yyy", "zzz"]\n```\n\n如果只有一个session也需要用数组的形式 \n\n```\nchatgpt_session_token_list = ["xxxx"]\n```\n\n获取token得方法，打开Application选项卡 > Cookie，复制值`__Secure-next-auth.session-token`并将其粘贴到在`.env.dev`中`session_token`即可。不需要管Authorization的值。\n![](https://chrisyy-images.oss-cn-chengdu.aliyuncs.com/img/image-20221205094326498.png)\n\n### 密码方式\n\n密码登陆需要通过代理来配置，一般配置格式如下。\n\n```\nchatgpt_email_list = ["osyyjozylg@iubridge.com", "lgfo353p@linshiyouxiang.net"]\nchatgpt_passwd_list = ["yy123123", "yy123123"]\nchatgpt_proxy = "http://127.0.0.1:6152"\n```\n\n### 其他\n指令前缀，默认值为`chat`\n\n```\nchatgpt_command_prefix = "。"\n```\n\n\n\n# Todo\n\n- [ ] 返回值渲染为图片\n- [ ] 完善密码登陆\n',
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
