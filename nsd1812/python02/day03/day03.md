# py2_day03

## 模块

文件是物理上组织代码的形式，模块就是逻辑上组织代码的形式。模块名是文件名去掉.py。

### 导入模块

python导入模块时，将会从以下两个位置搜索模块：

- sys.path定义的路径
- PYTHONPATH环境变量定义的路径

```python
>>> import sys
>>> sys.path
['', '/usr/local/lib/python36.zip', '/usr/local/lib/python3.6', '/usr/local/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']
```

### 导入模块的方法

```python
# 常用的导入方法
>>> import os
>>> from time import strftime

# 不常用的导入方法
>>> import random, datetime
>>> import pickle as p
```

### 导入和加载

- import是导入
- load是加载。加载就是将模块中的代码运行一遍
- 不管导入多少次，只会加载一次。

### hashlib模块

计算哈希值的模块。

- hash哈希是单向加密的算法。

- 通过原始数据可以生成固定长度的乱码
- 原始数据相同，乱码也一定相同
- 原始数据有微小的不同，乱码也一定完全不同
- 不能通过乱码反推回原始数据
- 常用的算法有：md5、sha
- 经常用于：存储加密密码、文件完整性校验

```python
>>> import hashlib
>>> m = hashlib.md5(b'123456')
>>> m.hexdigest()
'e10adc3949ba59abbe56e057f20f883e'

# 如果需要计算的数据量非常大，可以分批量进行更新
>>> m1 = hashlib.md5()
>>> m1.update(b'12')
>>> m1.update(b'34')
>>> m1.update(b'56')
>>> m1.hexdigest()
'e10adc3949ba59abbe56e057f20f883e'
```

### tarfile模块

实现归档压缩功能，支持gzip、bzip2、lzma格式的压缩。

```python
>>> import tarfile
>>> tar = tarfile.open('/tmp/demo/myfile.tar.gz', 'w:gz')
>>> tar.add('/etc/security')
>>> tar.add('/etc/hosts')
>>> tar.close()

>>> tar = tarfile.open('/tmp/demo/myfile.tar.gz', 'r')
# 不指定解压目标，默认解压到当前目录
>>> tar.extractall('/tmp/demo')
>>> tar.close()
```











