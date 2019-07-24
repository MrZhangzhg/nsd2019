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

创建记录有两种方法：

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











