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







