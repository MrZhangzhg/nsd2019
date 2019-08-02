# nsd1903_python1_day03

## 文件对象

### 操作步骤：

1. 打开
2. 读写
3. 关闭

### 读取文本文件

```python
(nsd1903) [root@room8pc16 day02]# cp /etc/passwd /tmp/
>>> f = open('/tmp/passwd')   # 打开文件
>>> data = f.read()   # 默认读取全部内容
>>> data
>>> print(data)
>>> data = f.read()
>>> data
''
>>> f.close()   # 关闭文件

>>> f = open('/tmp/passwd')
>>> f.read(4)   # 读取4字节
'root'
>>> f.read(3)
':x:'
>>> f.readline()   # 读取一行
'0:0:root:/root:/bin/bash\n'
>>> f.readline()
'bin:x:1:1:bin:/bin:/sbin/nologin\n'
>>> f.readlines()   # 将所有行读出来，放到列表中，每行是列表的一项
>>> f.close()

# 读文本文件使用最多的方式是for循环
>>> f = open('/tmp/passwd')
>>> for line in f:
...   print(line, end='')
>>> f.close()
```

### 以bytes方式读取文件

1个16进制数，正好对应4位2进制：

```python
0b0000 <-> 0x0
0b1111 <-> 0xF
```

读取任何文件都可以用bytes方式打开。读取文件内容时，如果是文本内容，将会以字符的形式显示，如果不能转成字符，将会直接显示16进制数。

```python
>>> f = open('/tmp/passwd', 'rb')
>>> f.read(4)
b'root'
>>> f.close()

>>> f = open('/bin/ls')
>>> f.read(10)   # 读取时，python试图将内容转换成字符，但是失败了，报错
>>> f.close()

>>> f = open('/bin/ls', 'rb')
>>> f.read(10)
b'\x7fELF\x02\x01\x01\x00\x00\x00'
>>> f.close()
```















