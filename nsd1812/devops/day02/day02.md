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

















