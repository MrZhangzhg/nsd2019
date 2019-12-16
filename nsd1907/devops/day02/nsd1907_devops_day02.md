# nsd1907_devops_day02

## 邮件编程

- 发邮件时，两件事：准备邮件、发送邮件
- 准备邮件使用email模块
- 发送邮件使用smtplib模块

## JSON

- JSON(JavaScript Object Notation)
- JSON采用完全独立于语言的文本格式
- JSON成为理想的数据交换语言

```python
>>> import json
>>> adict = {'name': 'tom', 'age': 20}
>>> data = json.dumps(adict)  # 将字典转成json字符串
>>> type(data)
<class 'str'>
>>> data
'{"name": "tom", "age": 20}'
>>> len(data)
26
>>> jdata = json.loads(data)  # 将json字符串转成python数据类型
>>> type(jdata)
<class 'dict'>
>>> jdata
{'name': 'tom', 'age': 20}
>>> len(jdata)
2
```

天气预报查询：

实况天气：http://www.weather.com.cn/data/sk/城市代码.html

城市信息：http://www.weather.com.cn/data/cityinfo/城市代码.html

详细指数：http://www.weather.com.cn/data/zs/城市代码.html

在搜索引擎中输入“中国天气网城市代码”搜索城市代码



