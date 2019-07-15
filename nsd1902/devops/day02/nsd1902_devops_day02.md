# nsd1902_devops_day02

## 邮件

- 写邮件：email模块
- 发邮件：smtplib模块

### 写邮件

- 邮件正文
- 邮件的头部信息
  - 发件人
  - 收件人
  - 主题

### 发邮件

- 邮件服务器
  - 需要认证的服务器需要填用户名和密码
  - 服务器的地址在邮箱的“设置”中查询
  - 需要在邮件服务器的“设置”中允许客户端使用smtp
  - 客户端发邮件时，填写的是授权码
- 发件人
- 收件人

## JSON

- JSON(JavaScript Object Notation)
- 在网络中传输数据时，如果希望传递的数据是有结构的（不同的数据类型），就用到JSON了。
- JSON可以把任意类型的数据转成json字符串，反之亦然

```python
>>> import json
>>> adict = {'name': 'tom', 'age': 20}
# 将字典转换成json字符串
>>> json.dumps(adict)
'{"name": "tom", "age": 20}'
>>> jdata = json.dumps(adict)
>>> type(jdata)
<class 'str'>

# 将json字符串转换成对应的数据类型
>>> json.loads(jdata)
{'name': 'tom', 'age': 20}
```

json应用：获取天气情况

- 搜索“中国天气网 城市代码”

- 访问网址

  - ```python
    实况天气: http://www.weather.com.cn/data/sk/城市代码.html
    ```

  - ```python
    城市信息: http://www.weather.com.cn/data/cityinfo/城市代码.html
    ```

  - ```python
    详细指数: http://www.weather.com.cn/data/zs/城市代码.html
    ```

  如北京：

  http://www.weather.com.cn/data/sk/101010100.html

  ```python
  >>> from urllib import request
  >>> url = 'http://www.weather.com.cn/data/sk/101010100.html'
  >>> r = request.urlopen(url)
  >>> data = r.read()
  >>> json.loads(data)
  ```

查快递

```python
url = 'http://www.kuaidi100.com/query?type=%s&postid=%s'
# type是快递公司，postid是单号
>>> url = 'http://www.kuaidi100.com/query?type=youzhengguonei&postid=9893442769997'
>>> r = request.urlopen(url)
>>> data = r.read()
>>> json.loads(data)
```

下载并注册一个钉钉账号

## requests模块

### http常用的方法

- get：
  - 在浏览器中直接输出网址
  - 在网页中点击超链接
  - 在一些表单中进行提交查询，如通过搜索引擎进行搜索
- post：通过表单提交数据，如注册、登陆

requests模块针对不同的http方法，分别创建了相关的函数，实现与之对应的功能。

### requests应用

安装：

```shell
# cd requests_pkgs/
# pip3 install *

# 或在线安装
# pip3 install requests
```

应用：

```python
>>> import requests
>>> r = requests.get('http://www.sogou.com')
>>> r.text   # 访问文本内容

>>> r = requests.get('https://upload-images.jianshu.io/upload_images/7610279-f4563d12e2cc2c14.jpg')
>>> r.content   # 非文本内容
>>> with open('/tmp/myimg.jpg', 'wb') as fobj:
...   fobj.write(r.content)

>>> url = 'http://www.weather.com.cn/data/zs/101010100.html'
>>> r = requests.get(url)
>>> r.json()    # 乱码
>>> r.encoding  # 查看编码
'ISO-8859-1'
>>> r.encoding = 'utf8'   # 更换编码方式
>>> r.json()
```











