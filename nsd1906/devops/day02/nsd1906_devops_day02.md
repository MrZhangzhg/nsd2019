# nsd1906_devops_day02

## paramiko

- 实现ssh客户端功能

```python
(nsd1906) [root@room8pc16 day02]# pip install paramiko_pkgs/*
>>> import paramiko
>>> ssh = paramiko.SSHClient()   # 创建SSHClient对象
# 自动接收服务器发来的密钥，相当于是自动回答yes
>>> ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 登陆
>>> ssh.connect('192.168.1.10', username='root', password='123456')
# 执行命令
>>> result = ssh.exec_command('id root; id zhangsan')
# 分析返回结果，result是一个长度为3的元组
>>> len(result)
3
# result中的三项分别是输入、输出和错误的类文件对象。
>>> stdin, stdout, stderr = result
>>> out = stdout.read()  # 读取输出信息
>>> err = stderr.read()  # 读取错误信息
>>> out
b'uid=0(root) gid=0(root) \xe7\xbb\x84=0(root)\n'
>>> err
b'id: zhangsan: no such user\n'
>>> out.decode()   # 将bytes转为str
'uid=0(root) gid=0(root) 组=0(root)\n'
>>> ssh.close()  # 关闭连接
```

## 邮件编程

- 写邮件，使用email模块
- 发邮件，使用smtplib模块

## JSON

- JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式
- JSON采用完全独立于语言的文本格式,但是也使用了类似于C语言家族的习惯(包括C, C++, C#, Java,JavaScript, Perl, Python等)
- python只要将数据类型转成json格式，其他语言的程序接收后，还能转成它能理解的数据类型

```python
>>> import json
>>> adict = {'name': 'bob', 'age': 20}
>>> json.dumps(adict)
'{"name": "bob", "age": 20}'
>>> data = json.dumps(adict)  # 将字典转成json字符串
>>> type(data)   # 字符串可以通过网络发送
<class 'str'>
>>> rdata = json.loads(data)  # 将json字符串转换成字典
>>> type(rdata)
<class 'dict'>
>>> rdata
{'name': 'bob', 'age': 20}
```

## requests模块

- Requests是用Python语言编写的、优雅而简单的HTTP库
- Requests内部采用来urillib3
- 常用的HTTP方法
  - GET：浏览器中输入网址、点击超链接、表单的默认提交方式
  - POST：表单明确声明的方法，用于提交数据
  - put / delete / options / head
- requests模块为每种方法都创建了相关的函数。通过什么方法访问服务器，只要调用相关的函数即可。

```python
# 安装
(nsd1906) [root@room8pc16 day02]# pip install requests_pkgs/*

>>> import requests
>>> url1 = 'http://www.163.com'
>>> r = requests.get(url1)
>>> r.text  # r.text用于显示字符内容

>>> url2 = 'https://img02.sogoucdn.com/app/a/100520021/b037705221517c5d8ed43f6115aefe3b'   # 该地址是一个图片URL
>>> r2 = requests.get(url2)
>>> with open('/tmp/girl.jpg', 'wb') as fobj:
...   fobj.write(r2.content)  # 非字符内容用r2.content

# 查询天气
实况天气获取:http://www.weather.com.cn/data/sk/城市代码.html
城市信息获取:http://www.weather.com.cn/data/cityinfo/城市代码.html
详细指数获取:http://www.weather.com.cn/data/zs/城市代码.html
# 北京的城市代码： 101010100
>>> url3 = 'http://www.weather.com.cn/data/sk/101010100.html'
>>> r3 = requests.get(url3)
>>> r3.encoding   # 查看当前字符编码
'ISO-8859-1'
>>> r3.encoding = 'utf8'  # 修改编码
>>> r3.json()    # 返回json数据
{'weatherinfo': {'city': '北京', 'cityid': '101010100', 'temp''27.9', 'WD': '南风', 'WS': '小于3级', 'SD': '28%', 'AP': '100, 'njd': '暂无实况', 'WSE': '<3', 'time': '17:55', 'sm': '2.1'sRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}


# 查快递
>>> url = 'http://www.kuaidi100.com/query'
>>> param = {'type': 'yuantong', 'postid': '4182963481428'}
>>> r = requests.get(url, params=param)
>>> r.json()
# 浏览器上对应的url:
http://www.kuaidi100.com/query?type=yuantong&postid=4182963481428
```

### 钉钉机器人

- https://www.jianshu.com/p/a3c62eb71ae3

### 图灵机器人

https://www.jianshu.com/p/3c0436af6e92

登陆微信的模块：itchat

## zabbix

- 官方手册：https://www.zabbix.com/documentation/3.4/zh/manual
- 












