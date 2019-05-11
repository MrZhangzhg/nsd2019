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

## 列表

容器、可变、顺序

```python
>>> alist = [10, 80, 20, 60]
>>> alist.append(50)  # 追加
>>> alist.extend([15, 100])  # 将序列对象扩展到alist中
>>> alist
[10, 80, 20, 60, 50, 15, 100]
>>> alist.remove(20)  # 删除元素
>>> alist.index(60)  # 取出60的下标
2
>>> alist.reverse()  # 反转
>>> alist.insert(2, 60)  # 将60插入到下标为2的位置
>>> alist
[100, 15, 60, 50, 60, 80, 10]
>>> alist.sort()  # 升序排列
>>> alist.sort(reverse=True)  # 降序
>>> alist.count(60)  # 统计60出现的次数
2
>>> alist.pop()  # 默认弹出最后一项
10
>>> alist.pop(2)  # 弹出下标为2的项目
60
>>> alist.clear(）  # 清空列表
```

## 元组

容器、不可变、顺序

```python
>>> atuple = (100, 80, 60, 50, 15)
>>> atuple.count(30)
0
>>> atuple.index(50)
3
# 单元素元组，必须在结尾加逗号，否则不是元组
>>> a = (10)
>>> type(a)
<class 'int'>
>>> a
10
>>> a = (10,)
>>> type(a)
<class 'tuple'>
>>> a
(10,)
>>> len(a)
1
```



## 







