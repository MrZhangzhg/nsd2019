# nsd1812_devweb_day04

## api

### 在python shell中运行指令

```shell
(djenv) [root@room8pc16 mysite]# python manage.py shell
```

### 导入模型

```python
>>> from polls.models import Question, Choice
```

### 创建问题

- 实例化

```python
>>> q1 = Question(question_text='你期待哪家公司给你发Offer？', pub_date='2019-05-27 9:00:00')
>>> q1.save()
```









### 





























