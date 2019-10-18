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













