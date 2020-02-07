## ansible_django_project2

### 制作webadmin应用

#### url规划

```python
http://127.0.0.1/webadmin：显示主机信息
http://127.0.0.1/webadmin/add_hosts：添加主机
http://127.0.0.1/webadmin/add_modules：添加模块
http://127.0.0.1/webadmin/tasks：执行ansible任务
```

#### 编写模型

```python
# webadmin/models.py
from django.db import models

class HostGroup(models.Model):
    groupname = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=100)
    ipaddr = models.CharField(max_length=15)
    group = models.ForeignKey(HostGroup)
    
    def __str__(self):
        return "%s=>%s:%s" % (self.group, self.hostname, self.ipaddr)

class Module(models.Model):
    modluename = models.CharField(max_length=50)
    
    def __str__(self):
        return self.modluename

class Argument(models.Model):
    arg_text = models.CharField(max_length=200)
    module = models.ForeignKey(Module)
    
    def __str__(self):
        return "%s=>%s" % (self.module, self.arg_text)

(nsd1908) [root@localhost myansible]# python manage.py makemigrations
(nsd1908) [root@localhost myansible]# python manage.py migrate

# 将模型注册到后台管理界面
# webadmin/admin.py
from django.contrib import admin
from .models import HostGroup, Host, Module, Argument

for item in [HostGroup, Host, Module, Argument]:
    admin.site.register(item)

# 登陆到http://127.0.0.1/admin/，添加两个组和一些主机
```

#### 配置ansible

```python
(nsd1908) [root@localhost myansible]# mkdir ansi_cfg
(nsd1908) [root@localhost myansible]# cd ansi_cfg
(nsd1908) [root@localhost ansi_cfg]# vim ansible.cfg
[defaults]
inventory = ./dhosts.py
remote_user = root
# 实现到远程主机的免密登陆
(nsd1908) [root@localhost ansi_cfg]# ssh-keygen 
(nsd1908) [root@localhost ansi_cfg]# ssh-copy-id 127.0.0.1

(nsd1908) [root@localhost ansi_cfg]# touch dhosts.py
(nsd1908) [root@localhost ansi_cfg]# chmod 755 dhosts.py
```

#### 创建动态主机清单文件

```python
动态主机清单文件就是一个脚本，它必须输出以下格式：
{
    'dbservers': {'hosts': ['主机1', '主机2']},
    'webservers' {'hosts': ['主机3', '主机4']},
}

# vim dhosts.py
#!/root/nsd1908/bin/python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:////var/ftp/nsd2019/nsd1908/devweb/ansible_pro/myansible/db.sqlite3',
    encoding='utf8',
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class HostGroup(Base):
    __tablename__ = 'webadmin_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50), unique=True)

class Host(Base):
    __tablename__ = 'webadmin_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(100))
    ipaddr = Column(String(15))
    group_id = Column(ForeignKey('webadmin_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(Host.ipaddr, HostGroup.groupname).join(HostGroup)
    # print(qset.all())
    result = {}
    for ip, group in qset:
        if group not in result:
            result[group] = {}
            result[group]['hosts'] = []
        result[group]['hosts'].append(ip)
    print(result)
(nsd1908) [root@localhost ansi_cfg]# ./dhosts.py 
{'dbservers': {'hosts': ['127.0.0.1']}, 'webservers': {'hosts': ['127.0.0.1', '127.0.0.1']}}
(nsd1908) [root@localhost ansi_cfg]# ansible all -m ping
```

#### 制作webadmin首页

```python
# 通过ansible-cmdb生成信息
(nsd1908) [root@localhost ansi_cfg]# ansible all -m setup --tree /tmp/nsd1908out/
(nsd1908) [root@localhost ansi_cfg]# ansible-cmdb /tmp/nsd1908out/ > ../templates/hosts.html

```













