# NSD1909_DEVWEB_DAY05

## 查询

1. get方法：get必须返回一个实例，返回0或多个结果都会报错
2. filter方法：返回的是一个列表，列表可以是空的，也可以是很多实例

```python
(nsd1908) [root@localhost mysite]# python manage.py shell
>>> from polls.models import Question, Choice
>>> Question.objects.get(id=1)  # 返回实例
<Question: 问题: 你期待第一份工作的工资是多少？>
>>> Question.objects.get(id=10)  # 找不到，报错
>>> Question.objects.get(id__lt=10)  # id小于10的问题多于一个，报错

>>> Question.objects.filter(id=1)   # 返回实例列表
<QuerySet [<Question: 问题: 你期待第一份工作的工资是多少？>]>
>>> Question.objects.filter(id=10)  # 返回空列表
<QuerySet []>
>>> Question.objects.filter(id__lt=10)  # 返回几个实例构成的列表
<QuerySet [<Question: 问题: 你期待第一份工作的工资是多少？>, <Question: 问题: 你打算去哪个喜欢吃什么?>, <Question: 问题: 你一天吃几顿饭？>]>

```

