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

  













