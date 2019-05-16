# py02_day04

## re模块

```python
>>> import re
# 在进行匹配的时候，如果匹配到了，返回匹配对象，否则返回None
>>> re.match('f..', 'food')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> re.match('f..', 'seafood')
>>> print(re.match('f..', 'seafood'))
None

>>> re.search('f..', 'food')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> re.search('f..', 'seafood')
<_sre.SRE_Match object; span=(3, 6), match='foo'>
>>> m = re.search('f..', 'seafood')
>>> m.group()   # 返回匹配到的内容
'foo'

>>> re.search('f..', 'seafood is food')
<_sre.SRE_Match object; span=(3, 6), match='foo'>
>>> m = re.search('f..', 'seafood is food')
>>> m.group()
'foo'
>>> re.findall('f..', 'seafood is food')
['foo', 'foo']

>>> list(re.finditer('f..', 'seafood is food'))
[<_sre.SRE_Match object; span=(3, 6), match='foo'>, <_sre.SRE_Match object; span=(11, 14), match='foo'>]
>>> for m in re.finditer('f..', 'seafood is food'):
...     print(m.group())
... 
foo
foo

>>> re.split('-|\.', 'hello-world.tar.gz')
['hello', 'world', 'tar', 'gz']
>>> re.sub('X', 'tom', 'Hi X. Nice to meet you X.')
'Hi tom. Nice to meet you tom.'

# 当有大量内容需要匹配的时候，先把正则表达式的模式编译一下，将会有更好的执行效率
>>> patt = re.compile('f..')
>>> patt.search('seafood')
<_sre.SRE_Match object; span=(3, 6), match='foo'>
>>> patt.findall('seafood is food')
['foo', 'foo']
```

### Counter对象

```python
>>> from collections import Counter
>>> c = Counter()
>>> c.update('1.1.1.1')
>>> c
Counter({'1': 4, '.': 3})
>>> c1 = Counter()
>>> c1.update(['1.1.1.1'])
>>> c1
Counter({'1.1.1.1': 1})
>>> c1.update(['1.1.1.1'])
>>> c1.update(['1.1.1.1'])
>>> c1.update(['1.1.1.1'])
>>> c1.update(['1.1.1.2'])
>>> c1.update(['1.1.1.2'])
>>> c1.update(['1.1.1.2'])
>>> c1.update(['1.1.1.3'])
>>> c1.update(['1.1.1.3'])
>>> c1
Counter({'1.1.1.1': 4, '1.1.1.2': 3, '1.1.1.3': 2})
>>> c1.most_common(2)
[('1.1.1.1', 4), ('1.1.1.2', 3)]

```



## pymysql模块

### 更改安装源

python软件包的官方站点：https://pypi.org/

通过国内镜像站点安装软件包的设置：

```shell
[root@room8pc16 day04]# mkdir ~/.pip/
[root@room8pc16 day04]# vim ~/.pip/pip.conf 
[global]
index-url = http://mirrors.163.com/pypi/simple/
[install]  
trusted-host=mirrors.163.com
```

### 安装pymysql模块

```shell
# 在线安装
[root@room8pc16 day04]# pip3 install pymysql

# 离线安装 
[root@room8pc16 zzg_pypkgs]# cd pymysql_pkgs/
[root@room8pc16 pymysql_pkgs]# pip3 install *
```

### 配置mysql或mariadb

1. 安装
2. 启动
3. 修改密码
4. 创建数据库

```shell
[root@room8pc16 ~]# yum install -y mariadb-server
[root@room8pc16 ~]# systemctl start mariadb
[root@room8pc16 ~]# mysql -uroot -ptedu.cn
MariaDB [(none)]> CREATE DATABASE nsd1812 DEFAULT CHARSET utf8;
```





