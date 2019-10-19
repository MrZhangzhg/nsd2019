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









