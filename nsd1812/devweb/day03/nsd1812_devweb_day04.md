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

- 使用objects管理器

django为每一个ORM类都创建了名为objects的管理器，可以通过这个管理器的方法实现对表的管理。

```python
>>> q2 = Question.objects.create(question_text='从达内结业 后，你希望去哪个城市工作？ ', pub_date='2019-06-01 12:00:00')
```

### 创建选项

- 实例化

```python
>>> c1 = Choice(choice_text='腾讯', question=q1)
>>> c1.save()
```

- 使用管理器

```python
>>> c2 = Choice.objects.create(choice_text='华为', question=q1)
```

- 通过问题实例的管理器创建选项

问题和选项有主外键约束，这是一对多的关系，即一个问题可以有多个选项。每个问题的实例都有一个xxx_set管理器。问题的选项是Choice，那么管理器就是choice_set，如果选项的类名是XuanXiang，那么管理器的名称是xuanxiang_set。

```python
>>> c3 = q1.choice_set.create(choice_text='阿里巴巴')
```

### 删除选项

```python
>>> c3.delete()
```

### 修改问题

```python
>>> q2.question_text = '从达内结业后，你打算去哪个城市工作？'
>>> q2.save()
```

### 查询

```python
# 查询所有的问题
>>> Question.objects.all()
>>> for q in Question.objects.all():
...     print(q.pub_date)
... 
2019-05-25 17:22:00
2019-04-25 12:00:00
2019-05-27 09:24:00
2019-05-27 09:00:00
2019-06-01 12:00:00
>>> Question.objects.order_by('pub_date')  # 根据发布时间升序排列
>>> for q in Question.objects.order_by('pub_date'):
...     print(q.pub_date)
... 
2019-04-25 12:00:00
2019-05-25 17:22:00
2019-05-27 09:00:00
2019-05-27 09:24:00
2019-06-01 12:00:00
>>> Question.objects.order_by('-pub_date')  # 根据发布时间降序排列

# 获取某一个问题的实例
# get必须得到一个实例，否则报错。
>>> Question.objects.get(id=1)  # 返回1号问题
>>> Question.objects.get(id=10)  # 如果不存在，则报错
>>> Question.objects.get(id__gt=1)  # id>1的问题，不只一项，报错。

# 获取多个实例
# filter可以得到0到多个实例的集合
>>> Question.objects.filter(id=1)   # 具有一项的查询集
>>> Question.objects.filter(id=10)  # 查询集为空
>>> Question.objects.filter(id__gt=1)  # 查询集有多项
```

### 查询条件

查询条件采用的形式是“属性__操作符=值”，id=1实际上是id\_\_exact=1的简写。

```python
>>> Question.objects.filter(id__exact=1)  # 等于1
>>> Question.objects.filter(id__gt=1)  # 大于1
>>> Question.objects.filter(id__gte=1)   # 大于等于1
>>> Question.objects.filter(id__lt=1)   # 小于1
>>> Question.objects.filter(id__lte=1)   # 小于等于1

# 其他属性与数字属性类似，也是使用__
>>> Question.objects.filter(question_text__startswith='从达内')
>>> Question.objects.filter(pub_date__month=5)
```

## 完善首页

### 修改函数，取出所有的问题

```python
from polls.models import Question

def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})
```

### 修改模板，显示所有问题

```html
<!-- index.html -->
<body>
<div class="container">
    <h1>投票首页</h1>
    <div>
        <ol>
            {% for question in questions %}
                <li>
                    <a href="">{{ question.question_text }}</a>
                    {{ question.pub_date }}
                </li>
            {% endfor %}
        </ol>
    </div>
</div>
</body>
```

> 说明：{{var}}表示变量，{% %}是模板语法标签，在{}以外的是html语法。

### 为超链接加上具体的url

```html
<li>
    <a href="http://127.0.0.1/polls/{{ question.id }}/">{{ question.question_text }}</a>
    {{ question.pub_date }}
</li>
```





























