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











