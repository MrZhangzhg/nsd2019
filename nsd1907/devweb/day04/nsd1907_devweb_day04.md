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





```

