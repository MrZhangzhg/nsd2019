# nsd1909-devops-day02

## paramiko

- paramiko实现的是ssh功能

```python
# 本地安装
[root@localhost day02]# pip3 install zzg_pypkgs/paramiko_pkgs/*
# 在线安装
[root@localhost day02]# pip3 install paramiko

>>> import paramiko
>>> ssh = paramiko.SSHClient()  # 创建客户端实例
# 设置自动接受密钥
>>> ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 登陆服务器
>>> ssh.connect('192.168.113.133', username='root', password='redhat')
# 执行命令
>>> result = ssh.exec_command('id root; id dingjie')
>>> len(result)
3
# 执行命令的返回值是一个3元素元组。这3项分别是输入、输出和错误的类文件对象。类文件对象提供了read方法，可以读取其中的内容
>>> stdin, stdout, stderr = ssh.exec_command('id root; id dingjie')
>>> out = stdout.read()
>>> err = stderr.read()
>>> out
b'uid=0(root) gid=0(root) \xe7\xbb\x84=0(root)\n'
>>> err
b'id: dingjie: no such user\n'
>>> ssh.close()   # 关闭
>>> out.decode()  # 将bytes类型转为str类型
'uid=0(root) gid=0(root) 组=0(root)\n'
```

## 邮件

- 发送邮件使用SMTP协议，端口号25
- 准备邮件使用email模块
- 发送邮件使用smtplib模块

## JSON

- JavaScript Object Notation
- json应用

```python
>>> import json
>>> data = {'name': 'tom', 'age': 20}
# 发送之前，需要将数据转换成json字符串
>>> jdata = json.dumps(data)
>>> type(jdata)
<class 'str'>
>>> jdata
'{"name": "tom", "age": 20}'

# 接收到的数据，再通过loads转换成对应的数据类型
>>> jdata
'{"name": "tom", "age": 20}'
>>> info = json.loads(jdata)
>>> type(info)
<class 'dict'>
>>> info
{'name': 'tom', 'age': 20}
```

## requests模块

- 是用Python语言编写的、优雅而简单的HTTP库
- 内部采用来urillib3
- HTTP最常用的方法：
  - get：浏览器中输入url访问；页面中点击超链接；搜索引擎提交表单
  - post：一般用于表单提交数据，比如登陆、注册
- requests模块将每个HTTP的方法都创建出了对应的函数

### requests应用

- api：应用程序接口
- 中国天气网提供的接口
  - 实况天气:http://www.weather.com.cn/data/sk/城市代码.html
  - 城市信息:http://www.weather.com.cn/data/cityinfo/城市代码.html
  - 详细指数:http://www.weather.com.cn/data/zs/城市代码.html
  - 城市代码通过网络搜索

```python
# 安装
[root@localhost day02]# pip3 install requests

>>> import requests
# 文本形式的内容，使用text属性获取
>>> url1 = 'http://www.163.com'
>>> r1 = requests.get(url1)
>>> r1.text

# 非文本数据，使用content属性获取，bytes类型。文本数据也可以使用此种方式。
>>> url2 = 'http://world.people.com.cn/NMediaFile/2020/0217/MAIN202002171833000079364831028.JPG'
>>> r2 = requests.get(url2)
>>> r2.content
>>> with open('/tmp/a.jpg', 'wb') as fobj:
...   fobj.write(r2.content)

# json数据，通过json()方法获取
>>> url3 = 'http://www.weather.com.cn/data/sk/101010100.html'
>>> r3 = requests.get(url3)
>>> r3.json()   # 乱码，因为编码问题
{'weatherinfo': {'city': 'å\x8c\x97äº¬', 'cityid': '101010100', 'temp': '27.9', 'WD': 'å\x8d\x97é£\x8e', 'WS': 'å°\x8fäº\x8e3çº§', 'SD': '28%', 'AP': '1002hPa', 'njd': 'æ\x9a\x82æ\x97\xa0å®\x9eå\x86µ', 'WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}
>>> r3.encoding  # 查看当前编码
'ISO-8859-1'
>>> r3.encoding = 'utf8'   # 修改编码
>>> r3.json()
{'weatherinfo': {'city': '北京', 'cityid': '101010100', 'temp': '27.9', 'WD': '南风', 'WS': '小于3级', 'SD': '28%', 'AP': '1002hPa', 'njd': '暂无实况', 'WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}
```

- 传参

```python
>>> kd_url = 'http://www.kuaidi100.com/query'
>>> params = {'type': 'youzhengguonei', 'postid': '9893442769997'}
>>> r = requests.get(kd_url, params=params)
>>> r.json()
```

- 修改请求头

```python
>>> js_url = 'http://www.jianshu.com'
>>> r = requests.get(js_url)
>>> r.text   # 403 forbidden

>>> r = requests.get(js_url, headers=headers)
>>> r.text    # 正常内容
```









