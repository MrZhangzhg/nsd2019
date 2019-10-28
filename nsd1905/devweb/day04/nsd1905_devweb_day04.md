# nsd1905_devweb_day04

## django api

```python
# 使用python shell
(nsd1905) [root@room8pc16 mysite]# python manage.py shell
>>> from polls.models import Question, Choice
# 在表中添加记录，方法一：Qeustion实例
>>> q1 = Question(question_text='你期待哪个公司给你发Offer？', pub_date='2019-10-28')
>>> q1.save()
# 在表中添加记录，方法二：
# django为每一个class都创建了一个名为objects的管理器，通过这个管理可以实现对模型的操作，如增删改查等
>>> q2 = Question.objects.create(question_text='毕业聚餐去哪里？', pub_date='2019-10-28 10:00:00')

# 添加选项，方法一：
>>> c1 = Choice(choice_text='阿里巴巴', question=q1)
>>> c1.save()
# 添加选项，方法二：
>>> c2 = Choice.objects.create(choice_text='腾讯', question=q1)
# 添加选项，方法三：每个问题的实例都有一个名为choice_set的管理器，通过它，可以反向创建选项实例。管理器的名字构成：选项class名_set，全部小写字母。如果选项class是XuanXiang，那么问题实例的管理器名，就叫xuanxiang_set
>>> c3 = q1.choice_set.create(choice_text='达内')

# 查询所有的问题,返回所有问题实例的列表
>>> qset1 = Question.objects.all()
>>> qset1
>>> qset1[0]
<Question: 问题: 第一份工作，你期待的工资是多少？>
>>> q1 = qset1[0]
>>> q1.question_text
'第一份工作，你期待的工资是多少？'
>>> q1.pub_date
datetime.datetime(2019, 10, 26, 16, 49)
>>> q1.id  # 没有在模型中声明主键，django自动添加名为id的主键
1
>>> for q in qset1:
...   print(q.question_text, q.pub_date)
... 

# 排序，默认是升序排列
>>> qset2 = Question.objects.order_by('pub_date')
>>> for q in qset2:
...   print(q.question_text, q.pub_date)
... 
你计划去哪个城市工作？ 2019-10-01 12:00:00
第一份工作，你期待的工资是多少？ 2019-10-26 16:49:00
你期待哪个公司给你发Offer？ 2019-10-28 00:00:00
毕业聚餐去哪里？ 2019-10-28 10:00:00
# 降序排列
>>> qset3 = Question.objects.order_by('-pub_date')
>>> for q in qset3:
...   print(q.question_text, q.pub_date)
... 
毕业聚餐去哪里？ 2019-10-28 10:00:00
你期待哪个公司给你发Offer？ 2019-10-28 00:00:00
第一份工作，你期待的工资是多少？ 2019-10-26 16:49:00
你计划去哪个城市工作？ 2019-10-01 12:00:00

# get方法取出一个实例，如果多于一个实例或是0个，都报错
>>> Question.objects.get(id=10)  # 没有取到，报错
>>> Question.objects.get(id__lt=10)  # id小于10的，有4项，报错
>>> Question.objects.get(id=1)
<Question: 问题: 第一份工作，你期待的工资是多少？>

# filter方法取出实例列表，列表长度不限
>>> Question.objects.filter(id__lt=10)
<QuerySet [<Question: 问题: 第一份工作，你期待的工资是多少？>, <Questio>, <Question: 问题: 你期待哪个公司给你发Offer？>, <Question: 问题: 毕业聚餐去哪里？>]>
>>> Question.objects.filter(id__gt=10)
<QuerySet []>

# 过滤条件。在django中使用的方式是:属性__条件=值
>>> Question.objects.filter(id=1)  # 是以下方式的简写
>>> Question.objects.filter(id__exact=1)
>>> Question.objects.filter(id__gt=1)  # id>1
>>> Question.objects.filter(id__lt=3)  # id<3
>>> Question.objects.filter(id__lte=3) # id<=3
>>> Question.objects.filter(id__gte=1) # id>=1
>>> Question.objects.filter(pub_date__year=2019)# pub_date.year=2019
>>> Question.objects.filter(pub_date__day=28) # pub_date.day=28
# question_text.startswith('你')
>>> Question.objects.filter(question_text__startswith='你')

```

















