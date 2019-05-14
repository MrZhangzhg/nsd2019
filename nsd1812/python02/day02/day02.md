# py02_day02

## 函数

函数创建没有先后关系，只要在调用时，所有的函数已经存在即可

```python
>>> def foo():
...     print('in foo')
...     bar()
... 
>>> def bar():
...     print('in bar')
... 
>>> foo()
in foo
in bar
```

### 函数参数

- 只有一个参数名，称作位置参数
- 参数形式是key=val，称作关键字参数

```python
>>> def get_age(name, age):
...     print('%s is %s years old' % (name, age))
... 
>>> get_age('bob', 20)   # OK
bob is 20 years old
>>> get_age()   # Error，参数太少
>>> get_age('bob', 20, 100)   # Error，参数太多
>>> get_age(20, 'bob')  # 语法没有问题，但是语义不对
20 is bob years old
>>> get_age(age=20, name='bob')  # OK
bob is 20 years old
>>> get_age(age=20, 'bob')  # Error，关键字参数必须在后
>>> get_age(20, name='bob')  # Error，name得到了多个值
>>> get_age('bob', age=20)   # OK
bob is 20 years old
```

### 参数组

如果函数的参数个数是不固定的，可以使用参数组接收参数

- 在参数名前加\*表示参数是元组
- 在参数名前加\*\*表示参数是字典

```python
>>> def func1(*args):
...     print(args)
... 
>>> func1()
()
>>> func1('bob')
('bob',)
>>> func1('bob', 123)
('bob', 123)
>>> func1('bob', 123, 'hello', 'aaa')
('bob', 123, 'hello', 'aaa')
>>> def func2(**kwargs):
...     print(kwargs)
... 
>>> func2()
{}
>>> func2(name='bob', age=20)
{'name': 'bob', 'age': 20}

```









