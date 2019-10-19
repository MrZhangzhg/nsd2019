# nsd1905_devops_day02

## 邮件

- 准备邮件
- 发送邮件

## JSON

- JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式
- 基于JavaScript Programming Language
- JSON采用完全独立于语言的文本格式

```python
>>> import json
>>> user = {'user': 'bob', 'age': 20}
>>> json.dumps(user)
'{"user": "bob", "age": 20}'
>>> data = json.dumps(user)  # 把字典转换成json字符串
>>> type(data)
<class 'str'>

>>> json.loads(data)   # 把json字符串还原成字典
{'user': 'bob', 'age': 20}
>>> jdata = json.loads(data)
>>> type(jdata)
<class 'dict'>
>>> jdata
{'user': 'bob', 'age': 20}
```

API：Application Programing Interface应用程序编程接口

### 通过API和json查询天气情况

搜索“中国天气网 城市代码查询”，找到你想要查询区县的代码

实况天气获取:http://www.weather.com.cn/data/sk/城市代码.html

城市信息获取:http://www.weather.com.cn/data/cityinfo/城市代码.html

详细指数获取:http://www.weather.com.cn/data/zs/城市代码.html

```python
>>>from urllib import request
>>> import json
>>> html = request.urlopen('http://www.weather.com.cn/data/sk/101010100.html')
>>> data = html.read()
>>> data
b'{"weatherinfo":{"city":"\xe5\x8c\x97\xe4\xba\xac","cityid":"101010100","temp":"27.9","WD":"\xe5\x8d\x97\xe9\xa3\x8e","WS":"\xe5\xb0\x8f\xe4\xba\x8e3\xe7\xba\xa7","SD":"28%","AP":"1002hPa","njd":"\xe6\x9a\x82\xe6\x97\xa0\xe5\xae\x9e\xe5\x86\xb5","WSE":"<3","time":"17:55","sm":"2.1","isRadar":"1","Radar":"JC_RADAR_AZ9010_JB"}}'
>>> json.loads(data)
{'weatherinfo': {'city': '北京', 'cityid': '101010100', 'temp': '27.9',WD': '南风', 'WS': '小于3级', 'SD': '28%', 'AP': '1002hPa', 'njd': '暂无WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}
```

## requests模块

- requests是用Python语言编写的、优雅而简单的HTTP库
- requests内部采用来urillib3
- requests模块将http常用的方法都定义成了相应的函数，需要哪个方法调用相关函数即可
- HTTP最常用的方法
  - GET：浏览器中输入url、点击页面中的超链接、表单的默认行为（如搜索）
  - POST：表单提交数据给服务器，可以用POST

```python
(nsd1905) [root@room8pc16 ~]# pip install zzg_pypkgs/requests_pkgs/*
>>> import requests
>>> r = requests.get('http://www.163.com')
>>> r.text   # 查看文本内容用text属性

```





