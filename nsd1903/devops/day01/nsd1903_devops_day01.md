# nsd1903_devops_day01

## 多进程编程

- 解决效率问题
- 程序只是存储在磁盘上的可执行文件
- 进程可以看作是程序的一次执行，也可以说是加载到内存中的一系列指令
- 一个进程中还会包含一到多个线程
- 每个进程都有自己独立的运行环境
- 线程共享所在进程的运行环境
- windows系统不支持多进程
- python使用os.fork()实现多进程
  - os.fork()的返回值是数字
  - 父进程中，这个数字是非0值（子进程的PID号）
  - 子进程中， 这个数字是0

多进程编编程思路

- 明确父子进程的工作职责
- 父进程只负责生成子进程
- 子进程做具体的工作
- 子进程工作完毕后，需要彻底退出



## 多线程

- 主线程一般用于生成工作线程
- 工作线程作具体的工作，工作完后，自行退出
- 多线程没有僵尸进程的问题

## urllib模块

包含4个子模块，常用的是urllib.request和urllib.error模块

### urllib.request

```python
>>> from urllib import request
>>> html = request.urlopen('http://www.163.com')
>>> html.read(10)
b' <!DOCTYPE'
>>> html.readline()
b' HTML>\n'
>>> html.read()

>>> url = 'https://upload-images.jianshu.io/upload_images/12347101-9527fb424c6e973d.png'
>>> html = request.urlopen(url)
>>> data = html.read()
>>> with open('/tmp/myimg.jpeg', 'wb') as fobj:
...   fobj.write(data)
(nsd1903) [root@room8pc16 day01]# eog /tmp/myimg.jpeg
```















