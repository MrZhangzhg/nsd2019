# day04

python官方帮助文档

https://docs.python.org/zh-cn/3/  -> [标准库参考](https://docs.python.org/zh-cn/3/library/index.html) 

搜狗翻译 -> https://fanyi.sogou.com/

## 查看帮助

```python
>>> import shutil
>>> help(shutil)
>>> help(shutil.copy)
```

## subprocess模块

### 常用方法

```python
>>> import subprocess
>>> subprocess.run('ls')   # ls
>>> subprocess.run(['ls', '/home'])  # 没有shell环境
>>> subprocess.run('ls /home')   # FileNotFoundError

# 在shell环境中运行ls /home
>>> subprocess.run('ls /home', shell=True)
```

没有shell环境，就没有环境变量、命令扩展

```python
>>> rc = subprocess.run(['ls', '~'])
ls: 无法访问~: 没有那个文件或目录
CompletedProcess(args=['ls', '~'], returncode=2)
>>> rc.returncode   # 相当于是$?
2
>>> rc = subprocess.run('ls ~', shell=True)
>>> rc.returncode
```

### 获取输出

可以通过subprocess.PIPE将命令的错误和输出保存到stderr和stdout中。这两个参数是bytes类型。

```python
>>> rc = subprocess.run('id root; id wangwu', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
>>> rc.args  # 执行的指令
'id root; id wangwu'
>>> rc.stderr
b'id: wangwu: no such user\n'
>>> rc.stdout
b'uid=0(root) gid=0(root) \xe7\xbb\x84=0(root)\n'
```

### 字符串分为bytes类型和str类型

```python
>>> s1 = '达内'
>>> type(s1)
<class 'str'>
>>> b1 = s1.encode()   # 编码成bytes类型，使用utf8编码
>>> b1
b'\xe8\xbe\xbe\xe5\x86\x85'
>>> type(b1)
<class 'bytes'>
>>> b1.decode()   # 解码成str类型
'达内'
```



## 



