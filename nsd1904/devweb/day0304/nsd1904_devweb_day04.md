# nsd1904_devweb_day04

## 操作模型

```shell
# 加载python shell
(nsd1904) [root@room8pc16 mysite]# python manage.py shell
# 导入模型
>>> from polls.models import Question, Choice
# 创建问题实例，方法一：
>>> q1 = Question(question_text="你计划哪个城市工作？", pub_date="2019-09-27 10:00:00")
>>> q1.save()
# 创建问题实例，方法二：
# 每个实体类都有一个名为objects的管理器，通过这个管理器实现CRUD等操作
>>> q2 = Question.objects.create(question_text="你期待哪家公司给你发Offer？", pub_date="2019-10-01 12:00:00")

# 创建选项实例，方法一：
>>> c1 = Choice(choice_text="阿里巴巴", question=q2)
>>> c1.save()
# 创建选项实例，方法二：
>>> c2 = Choice.objects.create(choice_text="Tencent", question=q2)
# 创建选项实例，方法三：
# 问题和选项存在一对多的关系，一个问题可以有很多选项。每个问题的实例都有一个名为choice_set的管理器，通过它，可以创建选项。如果选项模型名为XuanXiang，那么问题的管理器就叫xuanxiang_set
>>> c3 = q2.choice_set.create(choice_text="jd")

# 查询：get必须只返回一个结果
>>> q1 = Question.objects.get(id=1)
>>> q1
<Question: 问题: 你期待的工资是多少？>

# 查询：all返回所有实例构成的实例列表
>>> Question.objects.all()

# 查询：filter返回0到多个实例构成的列表
>>> Question.objects.filter(id=10)
<QuerySet []>

# get和filter都采用相同的条件，只是返回值不一样。条件的书写方式使用双下划线来表示属性或方法，而不是句点
>>> s1 = 'Hello World'
>>> s1.startswith('He')
True
>>> Question.objects.filter(question_text__startswith="你")

>>> from datetime import datetime
>>> t = datetime.now()
>>> t.month
9
>>> Question.objects.filter(pub_date__month=9)
<QuerySet [<Question: 问题: 你期待的工资是多少？>, <Question: 问题: 十一ion: 问题: 你计划哪个城市工作？>]>

```











