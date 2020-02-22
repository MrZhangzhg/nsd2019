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

```













