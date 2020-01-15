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
- requests模块将每个http的方法都定义成了相关的函数

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

# 获取json内容
# 实况天气获取:http://www.weather.com.cn/data/sk/城市代码.html
# 城市信息获取:http://www.weather.com.cn/data/cityinfo/城市代码.html
# 详细指数获取:http://www.weather.com.cn/data/zs/城市代码.html
>>> url = 'http://www.weather.com.cn/data/sk/101010100.html'
>>> r = requests.get(url)
>>> r.json()  # 乱码
>>> r.encoding  # 查看字符编码
'ISO-8859-1'
>>> r.encoding = 'utf8'  # 修改字符编码
>>> r.json()
{'weatherinfo': {'city': '北京', 'cityid': '101010100', 'temp': '27.9',WD': '南风', 'WS': '小于3级', 'SD': '28%', 'AP': '1002hPa', 'njd': '暂无WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}
```

### 修改请求头

```python
>>> r = requests.get('http://www.jianshu.com')
>>> r.text  # 内容有<title>403 Forbidden</title>

# 修改头部的User-Agent为Firefox
>>> headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
>>> r = requests.get('http://www.jianshu.com', headers=headers)
>>> r.text   # 正常内容
```

### 传参

```python
# 查快递
>>> url = 'http://www.kuaidi100.com/query'
# type是快递公司名称，postid是单号
>>> params = {'type': 'shentong', 'postid': '773022616159695'}
>>> r = requests.get(url, params=params)
>>> r.json()
```

编写图灵机器人，帮你微信聊天

- 图灵机器人：https://www.jianshu.com/p/3c0436af6e92
- 微信模块：itchat https://www.jianshu.com/p/8f9c7e41eb55

## zabbix编程

- 官方手册：https://www.zabbix.com/documentation/3.4/zh/manual
- api本地路径：/var/www/html/zabbix/api_jsonrpc.php
- api url: http://x.x.x.x/zabbix/api_jsonrpc.php









