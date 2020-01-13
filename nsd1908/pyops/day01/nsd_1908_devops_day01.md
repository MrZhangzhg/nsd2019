# nsd_1908_devops_day01

## 多进程

- 编写的程序，默认是单进程、单线程的。程序只能按编写的序列一条条地扫行。
- 执行指令时，父进程将自身资拷贝一份，生成子进程，指令在子进程中运行，称作fork
- 在python中，os.fork()实现多进程
- 注意：windows不支持多进程编程
- os.fork()的返回值是数字。在父进程中这个数字是非0值（子进程的PID号），在子进程中，这个数字是0。

### 多进程编程思路

- 父进程只负责产生子进程
- 子进程负责做具体的工作
- 子进程工作结束后，需要彻底退出结束

## 多线程编程

- 程序是在磁盘上存储的一些可执行文件
- 程序运行时，将会在内存中出现一到多个进程。所以说，进程可以认为是加载到内存中的一系列指令。
- 一个进程中，可以包含多个线程。
- 每个进程都有自己独立的运行空间，但是线程共享进程的运行空间。
- windows支持线程

### 多线程编程思路

- 主线程只负责产生工作线程
- 工作线程负责做具体的工作

## urllib模块

- 包含了4个子模块：request / error / parse / robotparse
- 常用于http / ftp客户端编程

```python
>>> from urllib import request
>>> html = request.urlopen('http://www.163.com')
>>> html.read(10)
b' <!DOCTYPE'
>>> html.readline()
b' HTML>\n'
>>> html.readlines()
```

模拟客户端访问

```python
>>> url = 'http://www.jianshu.com'
>>> request.urlopen(url)
... ...
urllib.error.HTTPError: HTTP Error 403: Forbidden

# 设定请求头的User-Agent为Firefox
>>> headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
# 构建一个请求对象
>>> r = request.Request(url, headers=headers)
>>> html = request.urlopen(r)
>>> html.read()  # OK
```







