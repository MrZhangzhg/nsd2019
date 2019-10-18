# nsd1905_devops_day01

## 多进程

多进程使用os.fork()实现

os.fork()的返回值是数字，这个数字在父进程中是非0值（子进程的PID），在子进程中为0。

多进程的编程思路：

- 父进程仅用于生成子进程
- 子进程做具体的工作
- 子进程工作完成后，务必退出

## 多线程

- windows系统只支持多线程，不支持多进程
- 程序是计算机磁盘中存储的一些可执行文件
- 当程序运行时，就会创建一到多个进程。可以说进程是加载到内存中的一系列指令
- 一个进程可以由多个线程构成。
- 每个进程都有自己独立的运立的运行空间。线程共享进程的运行空间。
- 多线程的编程思路：
  - 主线程仅用于生成工作线程
  - 工作线程负责具体的工作

## urllib模块

- 主要用于http和ftp协议
- 它包括四个子模块：request、error、parse、robotparse

```python
>>> from urllib import request
>>> html = request.urlopen('http://www.163.com')
>>> html.readline()
b' <!DOCTYPE HTML>\n'
>>> html.read(10)
b'<!--[if IE'
>>> html.readlines()
```

如果只是下载，可以使用wget模块

```python
(nsd1905) [root@room8pc16 day01]# pip install wget
>>> import wget
>>> wget.download('https://img03.sogoucdn.com/app/a/100520021/1457d48c913eb448c5c5cabfaf799cf3', '/tmp/ttt.jpg')

```

修改请求头

```python
# 直接访问jianshu网站
>>> html = request.urlopen('http://www.jianshu.com')  # 报错
# 因为jianshu的服务器有反爬虫措施，在请求头里发现客户端不是常规则的浏览器则拒绝
# http协议的请求头通过User-Agent设置客户端浏览器
>>> headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
# 构建一个请求对象，修改头部信息
>>> r = request.Request('http://www.jianshu.com', headers=headers)
>>> html = request.urlopen(r)
>>> html.read()
```

url编码

url只允许一部分ascii字符，不允许的字符，使用时，必须先编码

```python
>>> url = 'https://www.sogou.com/web?query=国庆'
>>> html = request.urlopen(url)   # 报错

>>> url = 'https://www.sogou.com/web?query=' + request.quote('国庆')
>>> url
'https://www.sogou.com/web?query=%E5%9B%BD%E5%BA%86'
>>> html = request.urlopen(url)
```

## paramiko

- 实现了ssh协议
- 可以实现ssh远程控制
- 还可以实现sftp功能

```python
(nsd1905) [root@room8pc16 ~]# pip install zzg_pypkgs/paramiko_pkgs/*
>>> import paramiko
>>> ssh = paramiko.SSHClient()  # 创建实例
# 相当于是在询问是否接受服务器主机密钥时，自动回答yes
>>> ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
>>> ssh.connect('192.168.4.11', username='root', password='123456')
# 执行命令的返回值，是一个元组。元组中有三项，分别是输入、输出和错误的类文件对象
>>> stdin, stdout, stderr = ssh.exec_command('id root; id zhangsan')
# 获取输出和错误的内容
>>> out = stdout.read()
>>> err = stderr.read()
>>> out
b'uid=0(root) gid=0(root) \xe7\xbb\x84=0(root)\n'
>>> err
b'id: zhangsan: no such user\n'
>>> out.decode()
'uid=0(root) gid=0(root) 组=0(root)\n'
# 关闭连接
>>> ssh.close()
```











