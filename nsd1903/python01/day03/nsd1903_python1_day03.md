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

### 写文本文件

```python
>>> f = open('/tmp/passwd', 'w')   # 创建或清空文件
>>> f.write('hello world!\n')   # \n表示换行
13    # 表示共写入了13字节
>>> f.flush()  # 默认数据写到缓存，不会立即同步至磁盘，flush()立即写入磁盘
>>> f.writelines(['2nd line.\n', '3rd line.\n'])
>>> f.close()  # 关闭文件，数据也会同步到磁盘
```

### with语句

使用with打开文件，with语句结束后，文件自动关闭。

```python
>>> with open('/tmp/passwd') as f:
...   for line in f:
...     print(line, end='')
```

### 移动文件指针

```python
>>> f = open('/tmp/passwd', 'rb')
>>> f.tell()   # 返回文件指针位置，从文件开头到文件指针间的偏移量
0
>>> f.read(5)
b'hello'
>>> f.tell()
5
>>> f.seek(0, 0)   # 移动指针到文件开头
# seek第二个参数是相对位置，0表示开头，1表示当前位置，2表示结尾；第一个参数是偏移量
>>> f.seek(-6, 2)   # 移动指针到文件结尾前的第6个位置
>>> f.close()
```

练习：拷贝文件

```python
# 初步实现
f1 = open('/bin/ls', 'rb')
f2 = open('/tmp/ls', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
```

以上代码存在的问题

- 尽量使用变量，不要直接使用'/bin/ls'这样的直接量
- 变量名应该有意义，f1和f2这样的名称没有意义
- 读取数据时，一次将全部内容读入，有可能数据量太大













