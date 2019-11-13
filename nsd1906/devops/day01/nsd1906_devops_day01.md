# nsd1906_devops_day01

## 多进程

- windows不支持多进程
- os.fork返回值在父子进程中是不一样的
  - 父进程中，值非０（子进程的pid）
  - 子进程程中，值是０

- 多进程编程的思路
  - 父进程只负责生成子进程
  - 子进程做具体的工作
  - 子进程工作结束后，应该exit退出

## 多线程

- 各操作系统均支持
- 程序，就是在磁盘上存储的可执行文件
- 当程运行时，就会出现进程。可以说，进程就是加载内存中的一系列指令。每个进程都拥有自己独立的运行空间。
- 进程还可以拥有多个线程。同一进程内的所有线程，共享进程的运行空间。
- 多线程没有僵尸进程的问题
- 多线程的编程思路：
  - 主线程（类似于父进程），负责生成工作线程
  - 工作线程（类似于子进程），做具体的工作

## urllib模块

- 实现http客户端功能
- 包括4个子模块
  - request：最常用的模块
  - error：定义错误，实现异常
  - parse：用来解析和处理URL
  - robotparse：解析页面的robots.txt文件

```python
>>> from urllib import request
>>> url = 'http://www.163.com'
>>> html = request.urlopen(url)
>>> html.readline()
b' <!DOCTYPE HTML>\n'
>>> html.read(10)
b'<!--[if IE'
>>> html.readlines()
```

### 修改请求头

```python
>>> url = 'http://www.jianshu.com'
>>> html = request.urlopen(url)  # 403: Forbidden
# 简书它会做基本检查，发现请求不是正常的人为行为，将会拒绝
# 改变头部信息，骗过简书服务器，把客户端浏览器改为火狐
>>> url = 'http://www.jianshu.com'
>>> heads = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
>>> r = request.Request(url, headers=heads)
>>> html = request.urlopen(r)
>>> hrml.read()
```











