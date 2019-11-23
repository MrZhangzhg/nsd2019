# nsd1906_devweb_day04

## Model

```python
# 使用python shell
(nsd1906) [root@room8pc16 mysite]# python manage.py shell
# 导入模型
>>> from polls.models import Question, Choice

# 创建问题，方法一：直接创建实例
>>> q1 = Question(question_text="散伙饭去哪吃？", pub_date='2019-11-25')
>>> q1.save()

# 创建问题，方法二：使用objects管理器。django为每个实体类都创建了一个名为objects的管理，通过它的方法可以实现对模型的增删改查等操作。
# get_or_create是，如果没有相关记录则创建，如果库中已有相关记录则取出。
# get_or_create得到的是元组：(问题实例，True/False)
>>> q2 = Question.objects.get_or_create(question_text="你打算到哪 个城市找工作？", pub_date="2019-12-1")[0]


# 创建选项，方法一：
>>> c1 = Choice(choice_text='杭州', question=q2)
>>> c1.save()

# 创建选项，方法二：
>>> c2 = Choice.objects.get_or_create(choice_text='深圳', question=q2)[0]

# 创建选项，方法三：通过问题创建选项。问题和选项有一对多关系，一个问题有多个选项。每个问题的实例都有一个管理器，通过这个管理器可以创建选项。选项的class名叫Choice，那么管理器就叫choice_set；如果选项的class叫XuanXiang，那么管理器叫xuanxiang_set。
>>> c3 = q2.choice_set.get_or_create(choice_text='成都')[0]


# 查询
# 取出所有的问题，返回所有问题实例构成的列表
>>> Question.objects.all()
# 取出所有的问题，按发布时间升序排列
>>> Question.objects.order_by('pub_date')
# 取出所有的问题，按发布时间降序排列
>>> Question.objects.order_by('-pub_date')
>>> for q in Question.objects.order_by('-pub_date'):
...   print(q.pub_date, q.question_text)

# 通过get取出满足条件的实例，如果结果不是一项则报错
>>> Question.objects.get(id=1)
<Question: 问题:第一份工作，你期待的工资是多少？>
# 通过filter取出满足条件的实例列表，列表中可以是0到多项
>>> Question.objects.filter(id=10)
<QuerySet []>
>>> Question.objects.filter(id=1)
<QuerySet [<Question: 问题:第一份工作，你期待的工资是多少？>]>

# 查询条件
# django中查询条件使用双下划线代替句点表示属性或方法
# id=1，实际上是id__exact=1的缩写
>>> Question.objects.filter(id__exact=1)
<QuerySet [<Question: 问题:第一份工作，你期待的工资是多少？>]>
# id>1的写法：
>>> Question.objects.filter(id__gt=1)
# id<2的写法：
>>> Question.objects.filter(id__lt=2)
<QuerySet [<Question: 问题:第一份工作，你期待的工资是多少？>]>
# pub_date.month==12的写法：
>>> Question.objects.filter(pub_date__month=12)
<QuerySet [<Question: 问题:你打算到哪个城市找工作？>]>
# 字符串方法举例，判断字符串是否以某些字符开头
>>> s1 = 'hello world'
>>> s1.startswith('he')
True
>>> Question.objects.filter(question_text__startswith='你')
<QuerySet [<Question: 问题:你期待哪家公司给你发Offer？>, <Question: 问题：你打算到哪个城市找工作？>]>


# 修改问题，只要将问题实例取出，重新赋值即可
>>> q = Question.objects.get(question_text='你期待哪家公司给你发Offer？')
>>> q.question_text = '你心仪的公司是哪家？'
>>> q.save()

# 删除，将问题实例取出，调用删除方法
>>> q = Question.objects.get(question_text='散伙饭去哪吃？')
>>> q.delete()

```











