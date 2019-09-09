# nsd1904_devops_day01

https://down.51cto.com/ -> 《mysql必知必会》《正则表达式必知必会》

DEVOPS：

- Development：开发
- Operations：运维

## 多进程编程

- 程序只不过是在磁盘上存储的一些可执行文件
- 当程序执行时，就会产生一到多个进程。进程可以认为是程序的一次执行，也可以说是加载到内存中的一系列指令
- 进程中还可以包含一到多个线程
- windows系统不支持多进程

### 多进程的编程思路

- 父进程仅仅用于生成子进程
- 子进程做具体的工作
- 子进程工作结束后，需要彻底结束。否则它还将再产生子进程

## 多线程编程

- 每个进程都有自己独立的运行空间
- 同一进程的多个线程共享进程的运行空间
- 多线程不会产生僵尸进程

### 多线程编程思路

- 主线程用于生成工作线程
- 工作线程负责做具体的工作

## urllib

- urllib有四个子模块，常用的是request和error

```python
>>> from urllib import request
>>> html = request.urlopen('http://www.163.com')
>>> html.read(10)
b' <!DOCTYPE'
>>> html.readline()
b' HTML>\n'
>>> html.readlines()

# 下载图片
>>> html = request.urlopen('https://img04.sogoucdn.com/app/a/100520021/edd13a25faf36d6c3df00809538ed449')
>>> data = html.read()
>>> type(data)
<class 'bytes'>
>>> with open('/tmp/dog.jpg', 'wb') as fobj:
...   fobj.write(data)

[root@room8pc16 weekend1]# eog /tmp/dog.jpg 

```

## wget模块

```python
(nsd1904) [root@room8pc16 day01]# pip install wget
>>> import wget
>>> wget.download('https://img02.sogoucdn.com/app/a/100520021/03b4fea0e30924f351a1276baf00e523', '/tmp/girl.jpg')
(nsd1904) [root@room8pc16 day01]# eog /tmp/girl.jpg 
```

### 修改请求头

```python
>>> url = 'http://www.jianshu.com'
>>> html = request.urlopen(url)   # 403禁止访问

# 修改请求头中的浏览器值，模拟Firefox
>>> header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
>>> r = request.Request(url, headers=header)
>>> html = request.urlopen(r)
>>> html.readline()
b'<!DOCTYPE html>\n'
```

## url数据编码

- url中只允许一部分ASCII码字符
- 其他字符必须经过编码

```python
>>> url = 'https://www.sogou.com/web?query=中国'
>>> html = request.urlopen(url)  # 报错

# URL编码
>>> url = 'https://www.sogou.com/web?query=' + request.quote('中国')
>>> url
'https://www.sogou.com/web?query=%E4%B8%AD%E5%9B%BD'
>>> html = request.urlopen(url)
>>> html.readline()
b'<!DOCTYPE HTML>\n'
```

## paramiko模块

安装

```python
# 安装方法一：在线安装
(nsd1904) [root@room8pc16 day01]# pip install paramiko
# 安装方法二：本地安装
(nsd1904) [root@room8pc16 day01]# pip install paramiko_pkgs/*
```

应用

```python
>>> import paramiko
# 创建ssh客户端
>>> ssh = paramiko.SSHClient()
# 自动接受服务器发来的密钥
>>> ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
>>> ssh.connect('192.168.4.4', username='root', password='123456')
# 在远程主机执行命令
>>> result = ssh.exec_command('id root; id zhangsan')
# 执行命令后的返回值有3项，分别是输入、输出和错误的类文件对象
>>> len(result)
3
>>> stdin, stdout, stderr = result
>>> out = stdout.read()
>>> err = stderr.read()
>>> out
b'uid=0(root) gid=0(root) \xe7\xbb\x84=0(root)\n'
>>> err
b'id: zhangsan: no such user\n'
>>> out.decode()   # 把bytes转成str
'uid=0(root) gid=0(root) 组=0(root)\n'
# 关闭连接
>>> ssh.close()
```













