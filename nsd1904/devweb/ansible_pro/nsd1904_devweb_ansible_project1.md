# nsd1904_devweb_ansible_project1

## 项目展示

### 运行nsd1903班ansible_pro项目

```shell
$ source ~/nsd1904/bin/activate
$ cd nsd2019/nsd1903/devweb/ansible_pro/myansible
$ python manage.py runserver
访问127.0.0.1:8000
```

### 功能说明

- http://127.0.0.1:8000/：首页，列出所有功能项
- http://127.0.0.1:8000/webadmin/：展示托管主机详细信息
- http://127.0.0.1:8000/webadmin/addhosts/：实现添加主机/组功能
- http://127.0.0.1:8000/webadmin/addmodules/：实现添加模块/参数功能
- http://127.0.0.1:8000/webadmin/tasks/：在指定的主机或组上执行管理任务

## 编写项目

### 项目初始化

1. 通过pycharm创建名为myansible的项目
2. 创建名为index和webadmin的应用

```shell
(nsd1904) [root@room8pc16 myansible]# python manage.py startapp index
(nsd1904) [root@room8pc16 myansible]# python manage.py startapp webadmin
```

3. 修改配置文件

```shell
# myansible/settings.py
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    ... ...
    'index',
    'webadmin',
]
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```







