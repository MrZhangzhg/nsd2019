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

>>> r = requests.get('https://img02.sogoucdn.com/app/a/100520021/8448941d79bb0542d65d3c8ca3f62bc0')
>>> r.content   # 查看bytes类型数据
>>> with open('/tmp/cat.gif', 'wb') as fobj:
...   fobj.write(r.content)

>>> r = requests.get('http://www.weather.com.cn/data/zs/101010100.html')
>>> r.json()  # json格式，使用r.json()方法。
# 如果查看时有乱码，首先查看字符集
>>> r.encoding
'ISO-8859-1'
>>> r.encoding = 'utf8'   # 修改字符集
>>> r.json()   # 再次查看，正常

# 修改请求头
>>> r = requests.get('http://www.jianshu.com')
>>> r.text   # 内容是403 forbidden

>>> header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
>>> r = requests.get('http://www.jianshu.com', headers=header)
>>> r.text   # 正常的内容
```

url分析：

https://www.sogou.com/web?query=linux+python&_asf=www.sogou.com&_ast=&w=01019900

以上URL，？左边是URL，？右边是传给该URL的参数。动态网站，一般一个URL对应一个函数，函数还可以接收参数。如以上网址对应的函数可以是：search(query, asf, ast,w)

```python
# 查快递
>>> url = 'http://www.kuaidi100.com/query'  # 快递100提供的API
# 接受的参数type是快递公司名字，postid是单号。由快递100提供
>>> param = {'type': 'zhongtong', 'postid': '75302716462400'}
>>> r = requests.get(url, params=param)
>>> r.json()
# 以上内容也可以在浏览器中访问：
http://www.kuaidi100.com/query?type=zhongtong&postid=75302716462400
```

### 钉钉机器人

- 钉钉是阿里巴巴开发的类似于微信的即时通信软件
- 钉钉机器人，就是创建一个群聊，在群聊中添加机器人
- 机器人会对应一个URL，只要访问该URL，并将相应的数据提交，就可以让机器人在群里发消息

搜索“钉钉机器人 开放平台”，找到钉钉机器人的官方手册：

https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq









