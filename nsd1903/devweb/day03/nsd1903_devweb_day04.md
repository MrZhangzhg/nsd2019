# nsd1903_devweb_day04

django在线文档：https://docs.djangoproject.com

## python shell

通过python shell操作模型

```python
(nsd1903) [root@room8pc16 mysite]# python manage.py shell
>>> from polls.models import Question, Choice
# 增加问题方法一：创建实例
>>> q1 = Question(question_text="你打算到哪个城市找工作？", pub_date="2019-8-20")
>>> q1.save()

# 增加问题方法二：通过objects管理器
# django为每个模型都创建了名为objects的管理器，通过objects可以实现对模型的各种操作
>>> q2 = Question.objects.create(question_text="放假出游去哪玩？", pub_date="2019-8-15")

# 创建选项方法一：创建实例
>>> c1 = Choice(choice_text="成都", question=q1)
>>> c1.save()

# 创建选项方法二：通过objects管理器
>>> c2 = Choice.objects.create(choice_text="石家庄", question=q1)

# 创建选项方法三：通过问题实例的choice_set创建
# 因为Question和Choice有一对多的关系，django为问题实例创建了choice_set管理器，用于找到该问题的所有选项。如选项类名为xuanxiang，那么就是xuanxiang_set。
>>> c3 = q1.choice_set.create(choice_text="上海")

# 查询操作也是通过模型的objects管理器实现的
# 获取所有的问题
>>> qset1 = Question.objects.all()
>>> for q in qset1:
...   print(q.id, q.question_text, q.pub_date)
... 
1 你期待的工资是多少？ 2019-08-21 17:26:00
2 你期待哪家公司给你发Offer？ 2019-08-01 12:00:00
3 散伙饭在哪吃？ 2019-08-10 18:00:00
4 你打算到哪个城市找工作？ 2019-08-20 00:00:00
5 放假出游去哪玩？ 2019-08-15 00:00:00

# get方法只能获取一个实例，0或多个实例都会报错
>>> q1 = Question.objects.get(question_text="你期待的工资是多少？")
>>> q1.id
1
>>> q1.question_text
'你期待的工资是多少？'
>>> q1.pub_date
datetime.datetime(2019, 8, 21, 17, 26)

# filter方法得到过滤后的集合，可以是0到多项，过滤条件与get的书写方式一样
>>> Question.objects.filter(id=1)
<QuerySet [<Question: 你期待的工资是多少？>]>
>>> Question.objects.filter(id=100)
<QuerySet []>

# 查询条件：在django中，查询时某一对象的属性不再使用句点表示，而是使用双下划线
>>> Question.objects.filter(id=1)   # 它是以下的简写
>>> Question.objects.filter(id__exact=1)
>>> Question.objects.filter(id__gt=2)   # id > 2
>>> Question.objects.filter(id__lt=2)   # id < 2
>>> Question.objects.filter(question_text__contains='工资')  # 包含工资
# 字符串以“你期待”开头
>>> Question.objects.filter(question_text__startswith="你期待")
# 发布时间的月份是8月的
>>> Question.objects.filter(pub_date__month=8)















```







