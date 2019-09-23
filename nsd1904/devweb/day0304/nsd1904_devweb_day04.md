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

```











