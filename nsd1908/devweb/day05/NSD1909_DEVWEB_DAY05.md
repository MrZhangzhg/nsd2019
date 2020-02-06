# NSD1909_DEVWEB_DAY05

## 查询

1. get方法：get必须返回一个实例，返回0或多个结果都会报错
2. filter方法：返回的是一个列表，列表可以是空的，也可以是很多实例

```python
(nsd1908) [root@localhost mysite]# python manage.py shell
>>> from polls.models import Question, Choice
>>> Question.objects.get(id=1)  # 返回实例
<Question: 问题: 你期待第一份工作的工资是多少？>
>>> Question.objects.get(id=10)  # 找不到，报错
>>> Question.objects.get(id__lt=10)  # id小于10的问题多于一个，报错

>>> Question.objects.filter(id=1)   # 返回实例列表
<QuerySet [<Question: 问题: 你期待第一份工作的工资是多少？>]>
>>> Question.objects.filter(id=10)  # 返回空列表
<QuerySet []>
>>> Question.objects.filter(id__lt=10)  # 返回几个实例构成的列表
<QuerySet [<Question: 问题: 你期待第一份工作的工资是多少？>, <Question: 问题: 你打算去哪个喜欢吃什么?>, <Question: 问题: 你一天吃几顿饭？>]>
```

3. django采用双下划线表示属性

```python
# 判断相等
>>> Question.objects.filter(id=1)  # 它实际上是以下方式的简写
>>> Question.objects.filter(id__exact=1)

# 其他判断
>>> Question.objects.filter(id__gt=1)   # id>1
>>> Question.objects.filter(id__gte=1)  # id>=1
>>> Question.objects.filter(id__lt=3)   # id<3
>>> Question.objects.filter(id__lte=3)  # id<=3
>>> Question.objects.filter(pub_date__month=1)  # 1月的问题
>>> Question.objects.filter(pub_date__month=2)  # 2月的问题
>>> s1 = 'hello'
>>> s1.startswith('he')
True
>>> Question.objects.filter(question_text__startswith='你')  # 以'你'开头的问题
>>> Question.objects.filter(question_text__contains='工作')  # 包含'工作'的问题

# 更多应用：https://docs.djangoproject.com/en/1.11/topics/db/queries/
```

### 制作投票首页

```python
# polls/views.py
from django.shortcuts import render
from .models import Question

# 每个函数至少需要一个参数，用于接收用户发来的请求
def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

# templates/index.html
# 在{}中的部分都是django的模板语法，{}外面的是html语法
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票首页</title>
</head>
<body>
<h1>投票首页</h1>
<ol>
# 模板支持循环语句，从问题列表中逐个取出问题实例，问题实例属性有id / question_text / pub_date
# {% url %}是模板中的标签，detail是在urls.py中定义的。question.id是传给detail的参数
    {% for question in questions %}
        <li>
            <a href="{% url 'detail' question.id %}" target="_blank">
                {{ question.question_text }}
            </a>
            {{ question.pub_date }}
        </li>
    {% endfor %}
</ol>
</body>
</html>
```

### 在模板页面中引入bootstrap

```python
# 将devweb/day02/static拷贝到polls目录中
# templates/index.html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票首页</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
</head>
<body>
<div class="container">
    <div id="linux-carousel" class="carousel slide">
        <ol class="carousel-indicators">
            <li class="active" data-target="#linux-carousel" data-slide-to="0"></li>
            <li data-target="#linux-carousel" data-slide-to="1"></li>
            <li data-target="#linux-carousel" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
            <div class="item active">
                <a href="http://www.sogou.com" target="_blank">
                    <img src="{% static 'imgs/first.jpg' %}">
                </a>
            </div>
            <div class="item">
                <img src="{% static 'imgs/second.jpg' %}">
            </div>
            <div class="item">
                <img src="{% static 'imgs/third.jpg' %}">
            </div>
        </div>
        <a href="#linux-carousel" data-slide="prev" class="carousel-control left">
            <span class="glyphicon glyphicon-chevron-left"></span>
        </a>
        <a href="#linux-carousel" data-slide="next" class="carousel-control right">
            <span class="glyphicon glyphicon-chevron-right"></span>
        </a>
    </div>
    <div>
        <h1 class="text-center text-warning">投票首页</h1>
        <ol class="h4">
            {% for question in questions %}
                <li>
                    <a href="{% url 'detail' question.id %}" target="_blank">
                        {{ question.question_text }}
                    </a>
                    {{ question.pub_date }}
                </li>
            {% endfor %}
        </ol>
    </div>
    <div class="h4 text-center">
        达内云计算学院 <a href="#">NSD1908</a>
    </div>
</div>

<script src="{% static 'js/jquery.min.js' %}"></script>
<script src="{% static 'js/bootstrap.min.js' %}"></script>
<script type="text/javascript">
    $('#linux-carousel').carousel({
        interval : 3000
    });
</script>
</body>
</html>
```

















