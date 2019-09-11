# nsd1904_devops_day02

## 邮件

- 准备邮件：email
- 发送邮件：smtplib

## JSON

- JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式
- JSON采用完全独立于语言的文本格式
- json.dumps将数据类型转成json字符串，用于网络传输
- json.loads将从网络上接收的字符串，转换成某种语言可理解的数据类型

```python
>>> import json
>>> adict = {'name': 'bob', 'age': 20}
>>> json.dumps(adict)
'{"name": "bob", "age": 20}'
>>> jstr = json.dumps(adict)
>>> type(jstr)
<class 'str'>
>>> json.loads(jstr)
{'name': 'bob', 'age': 20}
>>> data = json.loads(jstr)
>>> type(data)
<class 'dict'>
```

### 查天气预报

实况天气获取:http://www.weather.com.cn/data/sk/城市代码.html

城市信息获取:http://www.weather.com.cn/data/cityinfo/城市代码.html

详细指数获取:http://www.weather.com.cn/data/zs/城市代码.html

```python
>>> from urllib import request
>>> url = 'http://www.weather.com.cn/data/sk/101010100.html'
>>> html = request.urlopen(url)
>>> data = html.read()
>>> json.loads(data)
{'weatherinfo': {'city': '北京', 'cityid': '101010100', 'temp': '27.9',WD': '南风', 'WS': '小于3级', 'SD': '28%', 'AP': '1002hPa', 'njd': '暂无', 'WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}
```

## requests模块

HTTP常用方法：

- GET: 地址栏中输入网址、点击链超接、表单默认的提交行为
- POST: 表单提交数据

应用：

- 准备请求资源信息
- 发送请求
- 获取响应

```python
(nsd1904) [root@room8pc16 day02]# pip install requests_pkgs/*
>>> import requests
>>> url = 'https://img03.sogoucdn.com/app/a/100520021/9287d83fcb221ce7ea1868d2c7713f85'
>>> r = requests.get(url)   # 将响应信息保存到变量r
>>> with open('/tmp/g.jpg', 'wb') as fobj:
...   fobj.write(r.content)   # bytes类型数据通过r.content获取
(nsd1904) [root@room8pc16 day02]# eog /tmp/g.jpg 

>>> r = requests.get('http://www.163.com')
>>> r.text   # 文本数据，常用r.text方式取出

>>> url = 'http://www.weather.com.cn/data/zs/101010100.html'
>>> r = requests.get(url)
>>> r.encoding   # 显示当前字符编码
'ISO-8859-1'
>>> r.encoding = 'utf8'  # 修改字符编码
>>> r.json()   # 将json字符串转成相应的数据类型

```

钉钉机器人：https://www.jianshu.com/p/a3c62eb71ae3

搜索钉钉机器人开放平台: https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq

## zabbix













