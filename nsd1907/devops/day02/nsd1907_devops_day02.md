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

## requests模块

- Requests是用Python语言编写的、优雅而简单的HTTP库
- Requests内部采用来urillib3
- requests模块，将HTTP的方法定义好了与之对应的函数。需要使用什么方法访问URL，只要调用相关的函数即可。
- HTTP GET方法
  - 在浏览器的网址中书写url进行访问
  - 点击页面中的超链接
  - 有些表单的搜索
- HTTP POST方法：通过表单提交(隐私)数据，如登陆、注册

```python
(nsd1907) [root@room8pc16 day02]# pip install /var/ftp/pub/zzg_pypkgs/requests_pkgs/*
>>> import requests
>>> r = requests.get('http://www.163.com')
>>> r.text  # 文本内容使用r.text方法获取

>>> r = requests.get('https://i02picsos.sogoucdn.com/57bb0cff2c3d1a0e')
>>> r.content   # 非文本内容，使用r.content获取
>>> with open('/tmp/a.jpg', 'wb') as fobj:
...   fobj.write(r.content)
(nsd1907) [root@room8pc16 day02]# eog /tmp/a.jpg 

>>> url = 'http://www.weather.com.cn/data/zs/101010100.html'
>>> r = requests.get(url)
>>> r.json()   # 此时为乱码
>>> r.encoding  # 查看当前字符编码
'ISO-8859-1'
>>> r.encoding = 'utf8'   # 修改编码
>>> r.json()

```











