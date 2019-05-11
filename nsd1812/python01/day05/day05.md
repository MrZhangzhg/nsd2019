# day05

## 变量

### 全局变量

在函数外面定义的变量，从它定义的开始位置，一直到程序结束，都可见可用。

一般来说，变量的值自始至终都不需要变化，可以设置为全局变量。

### 局部变量

在函数内部定义的变量，只能在本函数内部使用。

## 生成随机字符串

```python
>>> import string
>>> import random
>>> all_chs = string.ascii_letters + string.digits
>>> result = [random.choice(all_chs) for i in range(8)]
>>> result
['V', '1', '1', 'R', '1', '7', 'm', '4']
>>> ''.join(result)
'V11R17m4'
>>> '-'.join(result)
'V-1-1-R-1-7-m-4'
>>> '##'.join(result)
'V##1##1##R##1##7##m##4'
```

## 原始字符串

作用：取消转义行为

```python
>>> win_path = 'c:\temp\newdir'
>>> print(win_path)  # \t成为tab，\n成为换行
c:	emp
ewdir
>>> wpath = r'c:\temp\newdir'
>>> print(wpath)
c:\temp\newdir
>>> wpath
'c:\\temp\\newdir'
```

## 字符串方法

```python
>>> s1 = ' \tHello World!  '
>>> s1.strip()  # 删除两端空白字符
'Hello World!'
>>> s1.lstrip()
'Hello World!  '
>>> s1.rstrip()
' \tHello World!'
>>> s2 = 'hao123'
>>> s2.center(30)
'            hao123            '
>>> s2.center(30, '*')
'************hao123************'
>>> s2.ljust(30, '#')
'hao123########################'
>>> s2.rjust(30, '#')
'########################hao123'
>>> s2.replace('h', 'H')  # 替换
'Hao123'
>>> s2.upper()
'HAO123'
>>> 'HAO123'.lower()
'hao123'
>>> s2.islower()  # 字母都是小写的吗
True
>>> s2.isdigit()  # 所有字符都是数字吗？
False
>>> s2.startswith('ab')   # 是以ab开头吗？
False
>>> s2.endswith('123')  # 是以123结尾吗？
True
>>> s1.count('l')  # 统计l出现的次数
3
>>> s1.index('l')  # 第一个l的下标
4
```



## 







