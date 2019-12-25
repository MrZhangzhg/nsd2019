# nsd1907_devweb_day04

## python api

```python
# 打开python shell
(nsd1907) [root@room8pc16 mysite]# python manage.py shell
# 导入模型 
>>> from polls.models import Question, Choice
# 创建问题方法一：直接创建实例
>>> q1 = Question(question_text='元旦放几天假？', pub_date='2019-12-25')
>>> q1.save()
# 创建问题方法二：使用objects管理器
# django为每个class都创建了一个名为objects的管理器，通过它可以实现对模型的增删改查操作
# get_or_create方法返回的是一个元组：(问题实例, True/False)。数据库中没有相关记录则创建，返回True；如果数据库中有记录则取出，返回Fase
result1 = Question.objects.get_or_create(question_text='春节放几天假', pub_date='2019-12-01')
>>> result1
(<Question: 问题: 春节放几天假>, True)
result2 = Question.objects.get_or_create(question_text='春节放几天假', pub_date='2019-12-01')
>>> result2
(<Question: 问题: 春节放几天假>, False)

# 创建选项方法一：实例化
>>> c1 = Choice(choice_text='1天', question=q1)
>>> c1.save()
# 创建选项方法二：通过objects管理器
>>> c_result1 = Choice.objects.get_or_create(choice_text='2天', question=q1)
# 创建选项方法三：通过问题实例的choice_set管理器创建
# 因为Question和Choice具有主外键约束，一个问题可以有很多选项。django为问题实例创建了名为xxxx_set的管理器（选项类名为Choice，管理器名为choice_set）。
>>> c_result2 = q1.choice_set.get_or_create(choice_text='3天')

# 修改、更新。只要将变量重新赋值即可
>>> q1.question_text = '你们公司元旦放几天假？'
>>> q1.save()

# 删除。调用实例的delete方法
>>> result1
(<Question: 问题: 春节放几天假>, True)
>>> q2 = result1[0]
>>> q2
<Question: 问题: 春节放几天假>
>>> q2.delete()
(1, {'polls.Choice': 0, 'polls.Question': 1})




```

