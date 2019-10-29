# nsd1905_ansible_project01

ansible项目展示：查看1904班项目

```shell
[root@room8pc16 ~]# source ~/nsd1905/bin/activate
(nsd1905) [root@room8pc16 ~]# cd /var/ftp/nsd2019/nsd1904/devweb/ansible_pro/myansible/
(nsd1905) [root@room8pc16 myansible]# python manage.py runserver
```

访问：http://127.0.0.1:8000/

功能说明：

http://127.0.0.1:8000/：项目首页，有4个超链接，可以访问主要的4个功能：主机信息、添加主机(组)、添加模块、执行任务

http://127.0.0.1:8000/webadmin/：显示所有主机的信息

http://127.0.0.1:8000/webadmin/addhosts/：添加主机、组

http://127.0.0.1:8000/webadmin/addmodules/：添加模块、参数

http://127.0.0.1:8000/webadmin/tasks/：在选定的主机/组上执行任务

