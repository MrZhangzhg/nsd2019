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

### 模板继承

为了实现不同页面具有一致的页风格，可以使用模板继承。将各个页面共性的内容，写到基础模板中，个性化的页面，写到具体的页面中。

```python
# 将index.html拷贝一份，名为base.html
(nsd1908) [root@localhost mysite]# cp templates/index.html templates/base.html

# 将base.html中共性的个性的内容删除，用{% block %}替代，共性内容保存
# templates/base.html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
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
    {% block content %}{% endblock %}
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

# 将index.html文件中的共性内容删除，个性内容放到相应的block中
# templates/index.html
{% extends 'base.html' %}
{% load static %}
{% block title %}投票首页{% endblock %}
{% block content %}
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
{% endblock %}
```

实现投票详情页和投票结果页的模板继承

```python
# templates/detail.html
{% extends 'base.html' %}
{% load static %}
{% block title %}投票详情{% endblock %}
{% block content %}
    <div>
        <h1 class="text-center text-warning">{{ question_id }}号问题的投票详情</h1>
    </div>
{% endblock %}


# templates/result.html
{% extends 'base.html' %}
{% load static %}
{% block title %}投票结果{% endblock %}
{% block content %}
    <div>
        <h1 class="text-center text-warning">{{ question_id }}号问题投票结果</h1>
    </div>
{% endblock %}

```

### 制作投票详情页

```python
# polls/views.py
def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'detail.html', {'question': question})

# templates/detail.html
{% extends 'base.html' %}
{% load static %}
{% block title %}投票详情{% endblock %}
{% block content %}
    <div>
        <h1 class="text-center text-warning">{{ question.id }}号问题的投票详情</h1>
        <h2>{{ question.question_text }}</h2>
        <form action="" method="post">
            {% csrf_token %}
            <div class="form-group">
                {% for choice in question.choice_set.all %}
                    <div class="radio">
                        <label>
                                <input type="radio" name="choice_id" value="{{ choice.id }}">
                                {{ choice.choice_text }}
                        </label>
                    </div>
                {% endfor %}
            </div>
            <input class="btn btn-primary" type="submit" value="提 交">
        </form>
    </div>
{% endblock %}

```

### 实现投票功能

要实现投票功能，需要执行一个函数；在django中，访问一个url，就可以执行函数了。函数的作用是把数据库中相应的选项票数加1。

```python
# polls/urls.py
... ...
    url(r'^(\d+)/vote/$', views.vote, name='vote'),
... ...

# polls/views.py
from django.shortcuts import render, redirect

def vote(request, question_id):
    # request是用户发来的请求，它是一个对象，其中它的POST属性是字典形式，对应表单post数据
    choice_id = request.POST.get('choice_id')
    question = Question.objects.get(id=question_id)  # 取出问题
    if choice_id:  # 如果choice_id非空
        choice = question.choice_set.get(id=choice_id)  # 通过问题取出选项
        choice.votes += 1
        choice.save()
    
    # 投票完成后跳转到投票结果页
    return redirect('result', question.id)

# templates/detail.html
... ...
        <form action="{% url 'vote' question.id %}" method="post">
... ...
```

### 制作投票结果页

```python
# polls/views.py
def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})

# templates/result.html
{% extends 'base.html' %}
{% load static %}
{% block title %}投票结果{% endblock %}
{% block content %}
    <div>
        <h1 class="text-center text-warning">{{ question.id }}号问题投票结果</h1>
        <table class="table table-bordered table-striped table-hover h4">
            <thead class="bg-primary">
                <tr>
                    <td colspan="2">{{ question.question_text }}</td>
                </tr>
            </thead>
            {% for choice in question.choice_set.all %}
                <tr>
                    <td>{{ choice.choice_text }}</td>
                    <td>{{ choice.votes }}</td>
                </tr>
            {% endfor %}
        </table>
        <div>
            <a href="{% url 'index' %}">返回首页</a>
        </div>
    </div>
{% endblock %}

```















