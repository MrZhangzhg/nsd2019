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









