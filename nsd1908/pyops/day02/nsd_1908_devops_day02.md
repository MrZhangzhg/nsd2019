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











