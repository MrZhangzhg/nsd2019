# nsd1903_devweb_day03

## django基础

- django是python编写的web框架
- 其他web框架还有flask、tornado

## MTV设计模式

- M: Model 数据库
- T: Template 模板 网页
- V: View视图 函数

```mermaid
graph LR
c(客户端)--访问-->s(服务器)
s-->url(路由系统URLConf)
url--调用-->v(视图函数Views)
v--crud-->db(Model数据模型)
db --返回结果-->v
v --渲染-->t(模板Template)
t --返回页面-->c

```

## 安装

离线

```shell
(nsd1903) [root@room8pc16 day02]# pip install zzg_pypkgs/dj_pkgs/*
```

在线

```shell
# pip install django==1.11.6
```

## 创建项目

- 项目代码需要放到目录中，所以创建项目时将会创建一个目录
- 通过django-admin命令创建

```shell
(nsd1903) [root@room8pc16 day03]# django-admin startproject mytest
```

- 通过pycharm创建：File -> New project -> 左边栏选django，Location填写项目路径,最后的目录名为mysite，注意项目解释器要选择正确
- 通过django自带的测试服务器启动项目

```shell
(nsd1903) [root@room8pc16 mysite]# python manage.py runserver
访问： http://127.0.0.1:8000
```

- 项目文件说明

```shell
(nsd1903) [root@room8pc16 mysite]# tree .
.                             # 项目的根目录
├── db.sqlite3                # 文件型数据库
├── manage.py                 # 项目管理文件
├── mysite                    # 项目管理目录
│   ├── __init__.py           # 项目初始化文件
│   ├── settings.py           # 配置文件
│   ├── urls.py               # URLConf路由文件
│   └── wsgi.py               # 部署时的配置文件
└── templates                 # 模板目录
```

- 搭建mariadb服务器







