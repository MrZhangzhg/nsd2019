# nsd1903_devweb_day04

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
>>> qset1 = Question.objects.all()
>>> for q in qset1:
...   print(q.id, q.question_text, q.pub_date)
... 
1 你期待的工资是多少？ 2019-08-21 17:26:00
2 你期待哪家公司给你发Offer？ 2019-08-01 12:00:00
3 散伙饭在哪吃？ 2019-08-10 18:00:00
4 你打算到哪个城市找工作？ 2019-08-20 00:00:00
5 放假出游去哪玩？ 2019-08-15 00:00:00

```







