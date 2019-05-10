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
>>> subprocess.run(['ls', '~'])
ls: 无法访问~: 没有那个文件或目录
CompletedProcess(args=['ls', '~'], returncode=2)
>>> rc.returncode   # 相当于是$?
2
>>> rc = subprocess.run('ls ~', shell=True)
>>> rc.returncode
```



## 



