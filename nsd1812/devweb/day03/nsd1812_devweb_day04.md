# nsd1812_devweb_day04

## api

### 在python shell中运行指令

```shell
(djenv) [root@room8pc16 mysite]# python manage.py shell
```

### 导入模型

```python
>>> from polls.models import Question, Choice
```

### 创建问题

- 实例化

```python
>>> q1 = Question(question_text='你期待哪家公司给你发Offer？', pub_date='2019-05-27 9:00:00')
>>> q1.save()
```

- 使用objects管理器

django为每一个ORM类都创建了名为objects的管理器，可以通过这个管理器的方法实现对表的管理。

```python
>>> q2 = Question.objects.create(question_text='从达内结业 后，你希望去哪个城市工作？ ', pub_date='2019-06-01 12:00:00')
```







### 





























