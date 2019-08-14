# nsd1903_devops_day02

## 邮件

- 准备邮件，使用email模块
- 发邮件，使用smtplib模块

## JSON

- JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。
- 可以通过网络传输各种类型的数据
- JSON采用完全独立于语言的文本格式，实现语言之间的数据交换

```python
>>> import json
>>> adict = {'name': 'bob', 'age': 20}
>>> json.dumps(adict)
'{"name": "bob", "age": 20}'
>>> data = json.dumps(adict)
>>> type(data)
<class 'str'>
>>> json.loads(data)
{'name': 'bob', 'age': 20}
>>> mydict = json.loads(data)
>>> type(mydict)
<class 'dict'>
```

### 查天气情况

- 实况：http://www.weather.com.cn/data/sk/城市代码.html
- 城市信息：http://www.weather.com.cn/data/cityinfo/城市代码.html
- 详细指数获取:http://www.weather.com.cn/data/zs/城市代码.html

```python
>>> url = 'http://www.weather.com.cn/data/sk/101010100.html'
>>> from urllib import request
>>> html = request.urlopen(url)
>>> data = html.read()
>>> data
b'{"weatherinfo":{"city":"\xe5\x8c\x97\xe4\xba\xac","cityid":"101010100","temp":"27.9","WD":"\xe5\x8d\x97\xe9\xa3\x8e","WS":"\xe5\xb0\x8f\xe4\xba\x8e3\xe7\xba\xa7","SD":"28%","AP":"1002hPa","njd":"\xe6\x9a\x82\xe6\x97\xa0\xe5\xae\x9e\xe5\x86\xb5","WSE":"<3","time":"17:55","sm":"2.1","isRadar":"1","Radar":"JC_RADAR_AZ9010_JB"}}'
>>> json.loads(data)
{'weatherinfo': {'city': '北京', 'cityid': '101010100', 'temp': '27.9',WD': '南风', 'WS': '小于3级', 'SD': '28%', 'AP': '1002hPa', 'njd': '暂无WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}
```

## requests模块

- requests是一个HTTP库
- requests内部采用来urillib3
- requests将HTTP各种方法提前定义成了函数，使用HTTP的某种方法访问web资源，只要调用相关函数即可
  - GET：通过浏览器访问网址、点击超链接、搜索表单提交
  - POST：通过表单提交数据（注册、登陆）

```python
# 安装 
(nsd1903) [root@room8pc16 day02]# pip install zzg_pypkgs/requests_pkgs/*
```

### requests应用

```python
# 文本内容使用text属性获取
>>> import requests
>>> r = requests.get('http://www.163.com')
>>> r.text

# 非文本bytes类型数据，通过content获取
>>> url = 'http://image.nmc.cn/product/2019/08/14/STFC/medium/SEVP_NMC_STFC_SFER_ER24_ACHN_L88_P9_20190814070002400.JPG'
>>> r = requests.get(url)
>>> with open('/tmp/weather.jpg', 'wb') as fobj:
...   fobj.write(r.content)
(nsd1903) [root@room8pc16 day02]# eog /tmp/weather.jpg 

# json数据使用json()方法
>>> url = 'http://www.weather.com.cn/data/sk/101010100.html'
>>> url = 'http://www.weather.com.cn/data/sk/101010100.html'
>>> r = requests.get(url)
>>> r.json()   # 乱码
{'weatherinfo': {'city': 'å\x8c\x97äº¬', 'cityid': '101010100', 'temp': '27.9', 'WD': 'å\x8d\x97é£\x8e', 'WS': 'å°\x8fäº\x8e3çº§', 'SD': '28%', 'AP': '1002hPa', 'njd': 'æ\x9a\x82æ\x97\xa0å®\x9eå\x86µ', 'WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}
>>> r.encoding   # 查看编码
'ISO-8859-1'
>>> r.encoding = 'utf8'   # 改变编码
>>> r.json()   # 正常显示
```

### 钉钉机器人

操作说明 ：https://www.jianshu.com/p/a3c62eb71ae3

搜索“钉钉机器人开发文档”  -> https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq



## zabbix编程

- zabbix api url
  - 将zabbix网站目录解压到/var/www/html/zabbix，
  - 则api url是http://ip/zabbix/api_jsonrpc.php
- zabbix官方手册：https://www.zabbix.com/documentation/3.4/zh/manual -> 19. API

API: 应用程序编程接口





