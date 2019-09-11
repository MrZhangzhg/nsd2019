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






