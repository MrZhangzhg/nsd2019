# nsd1907_devweb_day05

- 创建项目

```python
# 创建应用
(nsd1907) [root@room8pc16 myansible]# python manage.py startapp index
(nsd1907) [root@room8pc16 myansible]# python manage.py startapp webadmin
(nsd1907) [root@room8pc16 myansible]# ls
index  manage.py  myansible  templates  webadmin

# 修改配置
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
STATICFILES_DIRS = [   # 定义各个应用搜索静态文件路径，项目根目录的static目录
    os.path.join(BASE_DIR, "static"),
]

# 将前一个投票应用的static目录拷贝到当前项目根目录下
(nsd1907) [root@room8pc16 myansible]# cp -r ../../day0304/mysite/polls/static/ .

```

