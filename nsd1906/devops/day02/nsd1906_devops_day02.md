# nsd1906_devops_day02

## paramiko

- 实现ssh客户端功能

```python
(nsd1906) [root@room8pc16 day02]# pip install paramiko_pkgs/*
>>> import paramiko
>>> ssh = paramiko.SSHClient()   # 创建SSHClient对象
# 自动接收服务器发来的密钥，相当于是自动回答yes
>>> ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 登陆
>>> ssh.connect('192.168.1.10', username='root', password='123456')
# 执行命令
>>> result = ssh.exec_command('id root; id zhangsan')
# 分析返回结果，result是一个长度为3的元组
>>> len(result)
3
# result中的三项分别是输入、输出和错误的类文件对象。
>>> stdin, stdout, stderr = result
>>> out = stdout.read()  # 读取输出信息
>>> err = stderr.read()  # 读取错误信息
>>> out
b'uid=0(root) gid=0(root) \xe7\xbb\x84=0(root)\n'
>>> err
b'id: zhangsan: no such user\n'
>>> out.decode()   # 将bytes转为str
'uid=0(root) gid=0(root) 组=0(root)\n'
>>> ssh.close()  # 关闭连接
```







