### QScreenLock

###### © 2026 ExRFy Software Studio

A simple ScreenLock with Qt6(PySide6)


------

<img src="https://img.shields.io/badge/Python-3.13.8-blue">

<a href="https://space.bilibili.com/229776086"><img src="https://img.shields.io/badge/B站-ExRFy-light"></a>

<img src="https://img.shields.io/badge/使用提示-生产环境建议使用venv虚拟环境-red">

------

目录
* [介绍](#介绍)
* [构建](#构建)
    * [克隆项目文件](#克隆)
    * [准备环境](#准备)
    * [构建项目](#开始)
* [结语](#结语)

<p id="介绍"></p>

------=

# 介绍
这是一个用Qt6(PySide6)做的屏幕锁定

支持sha256密码，多密码解锁

<p id="构建"></p>
------

# 构建

<p id="克隆"></p>

1.克隆项目文件

使用git工具命令

```
git clone https://github.com/ExMC-Github/QScreenLock.git
```

或

直接下载压缩包

<p id="准备"></p>

2.准备环境

安装Python3并在安装过程中启用环境变量

进入QScreenLock目录

使用命令

```
pip install -r requirements.txt
```

安装预设的依赖列表

<p id="开始"></p>

3. 构建项目

使用命令

```
python build.py
```

使用pyinstaller打包应用程序

打包完成后，即可在dist目录看到QScreenLock.exe和QScreenLock-CreatePwd.exe

首次启动时默认密码是123456

可以用QScreenLock-CreatePwd.exe来追加密码或替换密码保存到pwd.json

在配置和测试完成后，即可使用

<p id="结语"></p>

------

# 结语

感谢您的体验与支持，希望您在体验便利的同时也可以贡献一份代码，为本项目的开源事业做出贡献！
