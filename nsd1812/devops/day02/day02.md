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

















