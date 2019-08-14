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















