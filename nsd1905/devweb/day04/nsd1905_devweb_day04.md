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

```

















