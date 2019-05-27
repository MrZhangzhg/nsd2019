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

### 创建选项

- 实例化

```python
>>> c1 = Choice(choice_text='腾讯', question=q1)
>>> c1.save()
```

- 使用管理器

```python
>>> c2 = Choice.objects.create(choice_text='华为', question=q1)
```

- 通过问题实例的管理器创建选项

问题和选项有主外键约束，这是一对多的关系，即一个问题可以有多个选项。每个问题的实例都有一个xxx_set管理器。问题的选项是Choice，那么管理器就是choice_set，如果选项的类名是XuanXiang，那么管理器的名称是xuanxiang_set。

```python
>>> c3 = q1.choice_set.create(choice_text='阿里巴巴')
```































