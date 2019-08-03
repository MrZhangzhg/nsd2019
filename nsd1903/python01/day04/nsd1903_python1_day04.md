# nsd1903_python1_day04

python官方手册页：https://docs.python.org/zh-cn/3/ -> 标准库参考

## shutil模块

主要实现复制、移动等操作

```python
import shutil

# 拷贝文件对象的方式，了解
f1 = open('/etc/passwd', 'rb')
f2 = open('/tmp/mima', 'wb')

shutil.copyfileobj(f1, f2)
f1.close()
f2.close()

# 直接拷贝文件 
>>> shutil.copyfile('/etc/shadow', '/tmp/sd')
'/tmp/sd'

# 将文件拷贝到目标目录，或指定目标位置及名字，常用
>>> shutil.copy('/etc/hosts', '/tmp/')
'/tmp/hosts'
>>> shutil.copy('/etc/hosts', '/tmp/zhuji.txt')
'/tmp/zhuji.txt'

# copy2相当于是cp -p  ， 常用
>>> shutil.copy2('/etc/hosts', '/tmp/zhj')
'/tmp/zhj'

# cp -r /etc/security /tmp/anquan， 常用
>>> shutil.copytree('/etc/security', '/tmp/anquan')
'/tmp/anquan'

# mv /tmp/anquan /var/tmp/anquan
>>> shutil.move('/tmp/anquan', '/var/tmp/anquan')
'/var/tmp/anquan'

# chown
>>> shutil.chown('/tmp/mima', user='bob', group='bob')

# rm -rf 
>>> shutil.rmtree('/var/tmp/anquan')
```

## subprocess模块

用于执行系统命令。

```python
# 在shell环境中执行命令ls ~
>>> subprocess.run('ls ~', shell=True)

>>> result = subprocess.run('ls abcd', shell=True)
ls: 无法访问abcd: 没有那个文件或目录
>>> result.returncode   # returncode就是$?
2

# 将输出保存到stdout中，将错误保存到stderr中
>>> result = subprocess.run('id root; id john', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> result.stdout
b'uid=0(root) gid=0(root) \xe7\xbb\x84=0(root)\n'
>>> result.stderr
b'id: john: no such user\n'
```

### bytes和str的转换

- 字母a对应的10进制数是97，2进制是0b01100001
- 一个字节是8位，一个ASCII字符可以用一个字节表示出来
- 所以bytes类型的数据，一个字节正好能表示成一个ASCII字符时，就显示成字符
- 汉字使用utf8编码，一个汉字需要占3字节。一个字节表示不出来汉字，所以一个汉字就需要使用三个以\x开头的16进制数表示
- str类型的字符串是引号括起来的部分
- bytes类型的字符串，以b''表示

```python
# bytes类型转成str类型
>>> result.stdout.decode()
'uid=0(root) gid=0(root) 组=0(root)\n'

>>> hi = '你好tom'
>>> hi.encode()   # str => bytes
b'\xe4\xbd\xa0\xe5\xa5\xbdtom'

>>> data = hi.encode()
>>> data
b'\xe4\xbd\xa0\xe5\xa5\xbdtom'
>>> data.decode()   # bytes => str
'你好tom'

```

## python语法风格

```python
# 链式多重赋值
>>> a = b = 10
>>> a
10
>>> b
10
>>> b = 20
>>> a
10

>>> alist = blist = [1, 2, 3]
>>> blist[-1] = 30
>>> blist
[1, 2, 30]
>>> alist
[1, 2, 30]

# 多元赋值
>>> a, b = 10, 20
>>> a
10
>>> b
20
>>> c, d = 'ab'
>>> c
'a'
>>> d
'b'
>>> e, f = [10, 20]
>>> e
10
>>> f
20
>>> m, n = (100, 200)
>>> m
100
>>> n
200

# 其他语言交换变量值的方法
>>> a, b = 10, 20
>>> t = a
>>> a = b
>>> b = t
>>> a
20
>>> b
10

# python交换两个变量值的方法 
>>> a, b = b, a
>>> a
10
>>> b
20
```

关键字

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

内建：

python创建的一些函数等。

https://docs.python.org/zh-cn/3/library/functions.html

### python模块布局

```python
#!/usr/local/bin/python     # 解释器
"""文档字符串

这是出现在help中的部分"""

import string   # 模块导入
import time

all_chs = string.ascii_letters + digits   # 全局变量定义
debug = True

class MyClass:   # 类定义
    pass

def func1():    # 函数定义
    pass

if __name__ == '__main__':
    mc = MyClass()
    func1()
```

### 编程思路

- 发呆。思考程序的运行方式（交互？非交互？），运行场景
- 思考程序有哪些功能，将这些功能写为函数，写出大体框架
- 编写程序主体。按顺序调用函数
- 编写函数内容

1. 运行方式

```shell
# python mkfile.py
文件名： /etc/hosts
文件已存在，请重试。
文件名：/etc/
文件已存在，请重试。
文件名：/tmp/abc.txt
请输入内容，输入end结束输入：
(end to quit)> hello world.
(end to quit)> ni hao.
(end to quit)> exit end
(end to quit)> end
# ls /tmp/abc.txt
abc.txt
# cat /tmp/abc.txt
hello world.
ni hao.
exit end
```

2. 编写功能函数

```python
def get_fname():


def get_content():


def wfile(fname, content):
```

3. 程序主体

```python
def get_fname():


def get_content():


def wfile(fname, content):


if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
```

4. 编写函数内容

```python
import os

def get_fname():
    while True:
        fname = input('文件名: ')
        # os.path.exists(fname) => 文件已存在返回True
        if not os.path.exists(fname):
            break
        print('文件已存在，请重试')

    return fname

def get_content():
    content = []

    print('请输入内容，输入end结束输入：')
    while True:
        line = input('(end to quit)> ')
        if line == 'end':
            break
        content.append(line + '\n')

    return content

def wfile(fname, content):
    with open(fname, 'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)

```



