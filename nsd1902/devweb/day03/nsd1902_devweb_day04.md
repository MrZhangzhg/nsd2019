# nsd1902_devweb_day04

修改实体类的声明，以便在后台中显示指定的字符串。

```python
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField()
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question)
    
    def __str__(self):
        return "%s=>%s" % (self.question, self.choice_text)
```

## django api

打开python shell

```python
(nsd1902) [root@room8pc16 mysite]# python manage.py shell
>>> from polls.models import Question, Choice
```

操作数据库

### 创建问题记录有两种方法：

- 实例化
- 在django中，每个class都有一个名为objects的管理器，通过这个管理器创建

```python
# 实例化
>>> q1 = Question(question_text='散伙饭去哪吃？', pub_date='2019-07-24 9:00:00')
>>> q1.save()

>>> from datetime import datetime
>>> dt1 = datetime.now()
>>> q2 = Question(question_text='散伙吃什么？', pub_date=dt1)
>>> q2.save()

# 通过objects管理器
>>> q3 = Question.objects.create(question_text="你打算到哪 个城市找工作？", pub_date="2018-12-1 12:00:00")
```

### 创建选项的三种方法

- 实例化
- 通过objects管理器
- 通过问题的choice_set创建选项

```python
# 实例化
>>> c1 = Choice(choice_text='北京', question=q3)
>>> c1.save()

# 通过objects管理器
>>> c2 = Choice.objects.create(choice_text='上海', question=q3)

# 因为问题和选项存在着一对多的关系，也就是一个问题可以对应多个选项。因为选项类名字是Choice，所以问题实例都有一个choice_set。如果选项类名字是XuanXiang，那么问题实例就有一个xuanxiang_set。choice_set也是一个管理器，它也有和objects一样的方法。
>>> c3 = q3.choice_set.create(choice_text='广州')
```

### 查询

查询的方法：

- get：要求必须返回一个实例，否则报错
- filter：返回0到多个实例的查询集

```python
>>> Question.objects.get(id=1)
<Question: 你期待的工资是多少？>
>>> Question.objects.filter(id=1)
<QuerySet [<Question: 你期待的工资是多少？>]>

>>> q1 = Question.objects.get(id=1)
>>> q1.question_text
'你期待的工资是多少？'
>>> q1.pub_date
datetime.datetime(2019, 7, 23, 9, 32)

>>> qset1 = Question.objects.filter(id=1)
>>> len(qset1)
1
>>> q2 = qset1[0]   # 取出下标为0的实例
>>> q2.question_text
'你期待的工资是多少？'
```







