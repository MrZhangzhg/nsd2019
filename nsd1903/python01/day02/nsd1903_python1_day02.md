# nsd1903_python1_day02

## 判断

- 数据类型也可以作为判断条件。任何值为0的数字都表示False，非0表示True；任何非空对象都表示True，空对象是False。

- 条件表达式

  ```python
  >>> a = 10
  >>> b = 20
  >>> if a <= b:
  ...   smaller = a
  ... else:
  ...   smaller = b
  ... 
  >>> smaller
  10
  
  # 将上面的判断改写为条件表达式（也叫三元运算符）
  >>> s = a if a <= b else b
  >>> s
  10
  ```

- 扩展if语句：多分支语句，满足某一条件就执行相应的语句块，其他条件不再判断。多分支只会执行一个分支。

  ```python
  if 条件1:
      语句块1
  elif 条件2:
      语句块2
  elif 条件3:
      语句块3
  ... ...
  else:
      语句块n
  ```

随机数模块

```python
>>> import random
# random.choice从给定的列表中随机选一项
>>> random.choice('abcdef')
'a'
>>> random.choice('abcdef')
'c'
>>> random.choice(['aaa', 'bb', 'cccc', 'ddd'])
'bb'
>>> random.choice(['aaa', 'bb', 'cccc', 'ddd'])
'ddd'
>>> random.choice(['aaa', 'bb', 'cccc', 'ddd'])
'ddd'
```

## while循环

python中循环分为while循环和for循环，当循环次数未知时，使用while循环，循环次数已知，使用for循环。

```python
while 循环条件:
    循环体内代码组
```

循环条件为真的时候，执行循环体内代码组。条件为真的情况和if判断一样。

### break和continue

- break：结束循环，循环体中break后续代码不再执行
- continue：跳过本次循环，循环体中continue后续代码不再执行

### else语句

循环的else语句：当循环被break，else语句不执行，否则执行



## for循环

### range函数

用于生成整数。

- 参数只给一个数字，表示结束数字，起始数字默认从0开始，结束数字不包含 

```python
>>> range(10)   # 生成range对象
range(0, 10)
>>> list(range(10))   # 转换成列表，只用于查看range能生成的数字
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for i in range(10):
...   print(i)
```

- 参数给两个数字，表示起始和结束数字，结束数字不包含 

```python
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

- range的第三个参数，是步长值

```python
>>> list(range(1, 11, 2))
[1, 3, 5, 7, 9]
>>> list(range(10, 0, -1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

## 列表解析

便捷的快速生成列表的方法

```python
>>> [10]
[10]
>>> [10 + 2]   # 表达式计算结果放到列表
[12]
>>> [10 + 2 for i in range(5)]   # 循环决定表达式计算几次
[12, 12, 12, 12, 12]
>>> [10 + i for i in range(1, 11)]  # 表达式可以用循环的变量
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> [10 + i for i in range(1, 11) if i % 2 == 1]  # 判断条件为真才保留计算结果
[11, 13, 15, 17, 19]

# 等价于以下代码：
>>> nums = []
>>> for i in range(1, 11):
...   if i % 2 == 1:
...     nums.append(10 + i)
... 
>>> nums
[11, 13, 15, 17, 19]
```

通过列表解析生成192.168.1.0/24网段的所有IP地址：

```python
>>> ['192.168.1.%s' % i for i in range(1, 255)]
```











