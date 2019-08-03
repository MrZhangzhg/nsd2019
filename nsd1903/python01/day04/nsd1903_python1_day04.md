# nsd1903_python1_day04

python官方手册页：https://docs.python.org/zh-cn/3/ -> 标准库参考

## shutil模块

主要实现复制、移动等操作

```python
import shutil

# 拷贝文件对象的方式，了解
f1 = open('/etc/passwd', 'rb')
f2 = open('/tmp/mima', 'wb')

shutil.copyfileobj(f1, f2)
f1.close()
f2.close()

# 直接拷贝文件 
>>> shutil.copyfile('/etc/shadow', '/tmp/sd')
'/tmp/sd'

# 将文件拷贝到目标目录，或指定目标位置及名字，常用
>>> shutil.copy('/etc/hosts', '/tmp/')
'/tmp/hosts'
>>> shutil.copy('/etc/hosts', '/tmp/zhuji.txt')
'/tmp/zhuji.txt'

# copy2相当于是cp -p  ， 常用
>>> shutil.copy2('/etc/hosts', '/tmp/zhj')
'/tmp/zhj'

# cp -r /etc/security /tmp/anquan， 常用
>>> shutil.copytree('/etc/security', '/tmp/anquan')
'/tmp/anquan'

# mv /tmp/anquan /var/tmp/anquan
>>> shutil.move('/tmp/anquan', '/var/tmp/anquan')
'/var/tmp/anquan'

# chown
>>> shutil.chown('/tmp/mima', user='bob', group='bob')

# rm -rf 
>>> shutil.rmtree('/var/tmp/anquan')
```

## subprocess模块

用于执行系统命令。

```python
# 在shell环境中执行命令ls ~
>>> subprocess.run('ls ~', shell=True)

>>> result = subprocess.run('ls abcd', shell=True)
ls: 无法访问abcd: 没有那个文件或目录
>>> result.returncode   # returncode就是$?
2

# 将输出保存到stdout中，将错误保存到stderr中
>>> result = subprocess.run('id root; id john', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> result.stdout
b'uid=0(root) gid=0(root) \xe7\xbb\x84=0(root)\n'
>>> result.stderr
b'id: john: no such user\n'
```

### bytes和str的转换

- 字母a对应的10进制数是97，2进制是0b01100001
- 一个字节是8位，一个ASCII字符可以用一个字节表示出来
- 所以bytes类型的数据，一个字节正好能表示成一个ASCII字符时，就显示成字符
- 汉字使用utf8编码，一个汉字需要占3字节。一个字节表示不出来汉字，所以一个汉字就需要使用三个以\x开头的16进制数表示
- str类型的字符串是引号括起来的部分
- bytes类型的字符串，以b''表示

```python
# bytes类型转成str类型
>>> result.stdout.decode()
'uid=0(root) gid=0(root) 组=0(root)\n'

>>> hi = '你好tom'
>>> hi.encode()   # str => bytes
b'\xe4\xbd\xa0\xe5\xa5\xbdtom'

>>> data = hi.encode()
>>> data
b'\xe4\xbd\xa0\xe5\xa5\xbdtom'
>>> data.decode()   # bytes => str
'你好tom'

```











