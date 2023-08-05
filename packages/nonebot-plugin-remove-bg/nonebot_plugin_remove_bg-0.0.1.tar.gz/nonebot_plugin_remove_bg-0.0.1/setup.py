# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_remove_bg']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0',
 'nonebot-adapter-onebot>=2.1.3,<3.0.0',
 'nonebot2>=2.0.0b5,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-remove-bg',
    'version': '0.0.1',
    'description': '适用于nonebot2 v11的基于trace.moe的动画截图场景追溯插件',
    'long_description': '<div align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n  <br>\n  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>\n</div>\n\n<div align="center">\n\n# nonebot_plugin_remove_bg\n  \n_✨ NoneBot 基于remove.bg的图片背景消除插件 ✨_\n  \n<a href="https://github.com/Ikaros-521/nonebot_plugin_remove_bg/stargazers">\n    <img alt="GitHub stars" src="https://img.shields.io/github/stars/Ikaros-521/nonebot_plugin_remove_bg?color=%09%2300BFFF&style=flat-square">\n</a>\n<a href="https://github.com/Ikaros-521/nonebot_plugin_remove_bg/issues">\n    <img alt="GitHub issues" src="https://img.shields.io/github/issues/Ikaros-521/nonebot_plugin_remove_bg?color=Emerald%20green&style=flat-square">\n</a>\n<a href="https://github.com/Ikaros-521/nonebot_plugin_remove_bg/network">\n    <img alt="GitHub forks" src="https://img.shields.io/github/forks/Ikaros-521/nonebot_plugin_remove_bg?color=%2300BFFF&style=flat-square">\n</a>\n<a href="./LICENSE">\n    <img src="https://img.shields.io/github/license/Ikaros-521/nonebot_plugin_remove_bg.svg" alt="license">\n</a>\n<a href="https://pypi.python.org/pypi/nonebot_plugin_remove_bg">\n    <img src="https://img.shields.io/pypi/v/nonebot_plugin_remove_bg.svg" alt="pypi">\n</a>\n<a href="https://www.python.org">\n    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n</a>\n\n</div>\n\n适用于nonebot2 v11的基于remove.bg的图片背景消除插件  \n调用的相关API源自:[https://www.remove.bg/api#api-reference](https://www.remove.bg/api#api-reference)   \n\n## 🔧 开发环境\nNonebot2：2.0.0b5  \npython：3.8.13  \n操作系统：Windows10（Linux兼容性问题不大）  \n编辑器：pycharm  \n\n## 💿 安装\n环境依赖`aiohttp`库   \n\n### 1. nb-cli安装（推荐）\n在你bot工程的文件夹下，运行cmd（运行路径要对啊），执行nb命令安装插件，插件配置会自动添加至配置文件  \n```\nnb plugin install nonebot_plugin_remove_bg\n```\n\n### 2. 本地安装\n先安装下 `aiohttp`  \n```\npip install aiohttp\n```\n将项目clone到你的机器人插件下的对应插件目录内（一般为机器人文件夹下的`src/plugins`），然后把`nonebot_plugin_remove_bg`文件夹里的内容拷贝至上一级目录即可。  \nclone命令参考（得先装`git`，懂的都懂）：\n```\ngit clone https://github.com/Ikaros-521/nonebot_plugin_remove_bg.git\n``` \n也可以直接下载压缩包到插件目录解压，然后同样提取`nonebot_plugin_remove_bg`至上一级目录。  \n目录结构： ```你的bot/src/plugins/nonebot_plugin_remove_bg/__init__.py```  \n\n\n### 3. pip安装\n```\npip install nonebot_plugin_remove_bg\n```  \n打开 nonebot2 项目的 ```bot.py``` 文件, 在其中写入  \n```nonebot.load_plugin(\'nonebot_plugin_remove_bg\')```  \n当然，如果是默认nb-cli创建的nonebot2的话，在bot路径```pyproject.toml```的```[tool.nonebot]```的```plugins```中添加```nonebot_plugin_remove_bg```即可  \npyproject.toml配置例如：  \n``` \n[tool.nonebot]\nplugin_dirs = ["src/plugins"]\nplugins = ["nonebot_plugin_remove_bg"]\n``` \n\n### 更新版本\n```\nnb plugin update nonebot_plugin_remove_bg\n```\n\n## 🔧 配置  \n\n### env配置\n```\n# nonebot_plugin_remove_bg 官方API KEY\nREMOVE_BG_API_KEY="XXXXXXXXXXXXXXXXXXXXXXXX"\n```\n|       配置项        | 必填 | 默认值  |                      说明                      |\n|:----------------:|:----:|:----:|:----------------------------:|\n| `REMOVE_BG_API_KEY` | 是 | `` | 注册官方账号申请API KEY |\n\n\n## 🎉 功能\n基于remove.bg，上传图片调用API消除背景后返回处理后的图片  \n\n## 👉 命令\n\n### 1、先发送命令，再发送图片（命令前缀请自行替换）\n先发送`/remove_bg`或`/去背景`或`/rm_bg`，等bot返回`请发送需要去除背景的图片喵~`后，发送需要去除背景的图片即可。  \n\n### 2、命令+图片\n编辑消息`/remove_bg[待去除背景的图片]`或`/去背景[待去除背景的图片]`或`/rm_bg[待去除背景的图片]`发送即可。 \n\n## ⚙ 拓展\n修改`__init__.py`中的`catch_str = on_command("remove_bg", aliases={"去背景", "rm_bg"})`来自定义命令触发关键词。  \n请求的参数有很多，可以自行修改或加到命令传参里面丰富功能。  \n\n## 📝 更新日志\n\n<details>\n<summary>展开/收起</summary>\n\n### 0.0.1\n\n- 插件初次发布\n\n\n</details>\n\n## 致谢\n\n- [remove.bg](https://www.remove.bg) - API来源  \n\n## 项目打包上传至pypi\n\n官网：https://pypi.org，注册账号，在系统用户根目录下创建`.pypirc`，配置  \n``` \n[distutils] \nindex-servers=pypi \n \n[pypi] repository = https://upload.pypi.org/legacy/ \nusername = 用户名 \npassword = 密码\n```\n\n### poetry\n\n```\n# 参考 https://www.freesion.com/article/58051228882/\n# poetry config pypi-token.pypi\n\n# 1、安装poetry\npip install poetry\n\n# 2、初始化配置文件（根据提示填写）\npoetry init\n\n# 3、微调配置文件pyproject.toml\n\n# 4、运行 poetry install, 可生成 “poetry.lock” 文件（可跳过）\npoetry install\n\n# 5、编译，生成dist\npoetry build\n\n# 6、发布(poetry config pypi-token.pypi 配置token)\npoetry publish\n\n```\n\n### twine\n\n```\n# 参考 https://www.cnblogs.com/danhuai/p/14915042.html\n#创建setup.py文件 填写相关信息\n\n# 1、可以先升级打包工具\npip install --upgrade setuptools wheel twine\n\n# 2、打包\npython setup.py sdist bdist_wheel\n\n# 3、可以先检查一下包\ntwine check dist/*\n\n# 4、上传包到pypi（需输入用户名、密码）\ntwine upload dist/*\n```',
    'author': 'Ikaros',
    'author_email': '327209194@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Ikaros-521/nonebot_plugin_remove_bg',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
