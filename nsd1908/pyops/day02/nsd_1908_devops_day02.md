# nsd_1908_devops_day02

## 邮件编程

- 准备邮件，使用email模块
- 发送邮件，使用smtplib模块

## JSON

- JSON(JavaScript Object Notation)是一种轻量级的数据交换格式
- JSON采用完全独立于语言的文本格式

```python
# 将字典转成json字符串
>>> import json
>>> adict = {'name': 'tom', 'age': 20}
>>> json.dumps(adict)
'{"name": "tom", "age": 20}'
>>> data = json.dumps(adict)
>>> type(data)
<class 'str'>

# 将json字符串转成python的数据类型
>>> json.loads(data)
{'name': 'tom', 'age': 20}
>>> jdata = json.loads(data)
>>> type(jdata)
<class 'dict'>
```

## requests模块

- 它是python语言编写的一个HTTP库
- 底层采用urllib3
- requests模块将每个httpd的方法都定义成了相关的函数

### http的方法

- GET：在浏览器中输入网址、点击超链接、一部分表单（如搜索）
- POST：常用在表单提交数据（如注册、登陆）
- HEAD
- OPTIONS
- DELETE

```python
# 安装
(nsd1908) [root@room8pc16 day02]# pip install /var/ftp/pub/zzg_pypkgs/requests_pkgs/*

# 获取文本内容
>>> import requests
>>> r = requests.get('http://www.163.com')
>>> r.text

# 获取非文本内容(bytes类型）
>>> r = requests.get('https://i01picsos.sogoucdn.com/9fe8e2323d7f76a4')
>>> r.content
>>> with open('/tmp/abc.jpg', 'wb') as fobj:
...   fobj.write(r.content)
(nsd1908) [root@room8pc16 day02]# eog /tmp/abc.jpg 

```







