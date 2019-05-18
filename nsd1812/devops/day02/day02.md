# tedu_cloud_devops_day02

## 下载网易首页上的所有图片

- 下载网易首页
- 遍历网易首页文件的内容，找出图片的URL
- 下载图片

## paramiko模块

实现ssh相关功能

### 安装

```shell
[root@room8pc16 zzg_pypkgs]# cd paramiko_pkgs/
[root@room8pc16 paramiko_pkgs]# pip3 install *
```

### 使用

```python
>>> import paramiko
>>> ssh = paramiko.SSHClient()
# 当远程主机发来密钥时，接受
>>> ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
>>> ssh.connect('192.168.4.4', username='root', password='123456')
>>> ssh.exec_command('mkdir /tmp/demo')
>>> ssh.close()
```

### exec_command的返回值

```python
>>> ssh.connect('192.168.4.4', username='root', password='123456')
>>> result = ssh.exec_command('id root; id john')
>>> len(result)
3
```

exec_command的返回值共三项，它们分别是输入、输出、错误，这三项都是类文件对象。那么它们都有read()方法。

```python
>>> result[1].read()
b'uid=0(root) gid=0(root) \xe7\xbb\x84=0(root)\n'
>>> result[2].read()
b'id: john: no such user\n'
```

## 邮件

发送邮件需要完成两个步骤：

1. 准备邮件
2. 发送邮件

## JSON

在网络中传输数据时，都是bytes类型的数据。如果希望把其他数据类型通过网络传递，可以使用json将其转换成json字符串，接收方接收后再将其转换回去。

```python
>>> import json
>>> adict = {'name': 'bob', 'age': 20}
>>> json.dumps(adict)
'{"name": "bob", "age": 20}'
# 在网络中发送该字典前，将其转换成json字符串
>>> jdata = json.dumps(adict)
>>> type(jdata)
<class 'str'>
# 接收方收到数据后，将json字符串转换回字典
>>> json.loads(jdata)
{'name': 'bob', 'age': 20}
>>> mydict = json.loads(jdata)
>>> type(mydict)
<class 'dict'>
```

### 查天气预报

- 实况天气获取:http://www.weather.com.cn/data/sk/城市代码.html
- 城市信息获取:http://www.weather.com.cn/data/cityinfo/城市代码.html
- 详细指数获取:http://www.weather.com.cn/data/zs/城市代码.html

城市代码搜索“中国天气网 城市代码”

如北京：http://www.weather.com.cn/data/sk/101010100.html

http://www.weather.com.cn/data/cityinfo/101010100.html

http://www.weather.com.cn/data/zs/101010100.html

```python
>>> import urllib
>>> from urllib import request
>>> bj = request.urlopen('http://www.weather.com.cn/data/sk/101010100.html')
>>> data = bj.read()
>>> data
b'{"weatherinfo":{"city":"\xe5\x8c\x97\xe4\xba\xac","cityid":"101010100","temp":"27.9","WD":"\xe5\x8d\x97\xe9\xa3\x8e","WS":"\xe5\xb0\x8f\xe4\xba\x8e3\xe7\xba\xa7","SD":"28%","AP":"1002hPa","njd":"\xe6\x9a\x82\xe6\x97\xa0\xe5\xae\x9e\xe5\x86\xb5","WSE":"<3","time":"17:55","sm":"2.1","isRadar":"1","Radar":"JC_RADAR_AZ9010_JB"}}'
>>> import json
>>> json.loads(data)
{'weatherinfo': {'city': '北京', 'cityid': '101010100', 'temp': '27.9', 'WD': '南风', 'WS': '小于3级', 'SD': '28%', 'AP': '1002hPa', 'njd': '暂无实况', 'WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}
```

## requests模块

它也是一个网络模块，底层采用urllib3。它把很多http的功能定义成了函数，需要某个功能，只要调用函数即可。

### http主要的方法：

- GET: 在浏览器中输入网址访问、点击超链接、通过表单查询
- POST: 一般用于提交隐私的表单数据

### requests应用

```shell
[root@room8pc16 zzg_pypkgs]# cd requests_pkgs/
[root@room8pc16 requests_pkgs]# pip3 install *
```

```python
>>> import requests
# 纯文本
>>> r = requests.get('http://www.sogou.com')
>>> r.text

# 非文本，如图片
>>> r = requests.get('https://img02.sogoucdn.com/app/a/100520020/64190bd002489844ea26062df90171fc')
>>> with open('/tmp/girl.jpg', 'wb') as fobj:
...     fobj.write(r.content)

# josn
>>> r = requests.get('http://www.weather.com.cn/data/sk/101010100.html')
>>> r.json()   # 乱码

# 编码
>>> r.encoding   # 查看默认编码
'ISO-8859-1'
>>> r.encoding = 'utf8'   # 修改字符编码
>>> r.json()
{'weatherinfo': {'city': '北京', 'cityid': '101010100', 'temp': '27.9', 'WD': '南风', 'WS': '小于3级', 'SD': '28%', 'AP': '1002hPa', 'njd': '暂无实况', 'WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}
```

### 查快递

查询快递的接口（API应用程序编程接口）：http://www.kuaidi100.com/query?type=%s&postid=%s

其中type是快递公司的名称，需要到相应的网站上查询，postid是单号

```python
>>> url = 'http://www.kuaidi100.com/query'
>>> params = {'type': 'zhongtong', 'postid': '94285844684'} 
>>> r = requests.get(url, params=params)
>>> r.json()
```

### 钉钉机器人

实现方式实际上不复杂，只是需要创建一个群，在群里添加聊天机器人。可以通过python程序，让机器人在群中发言。

搜索“钉钉机器人 开放平台”，找到官方手册页后，搜索“自定义机器人”

https://open-doc.dingtalk.com/microapp/serverapi3/iydd5h













