from django.shortcuts import render, redirect
from .models import Question

# Create your views here.
def index(request):
    # 用户的请求将会作为第一个参数传给函数，需要使用变量接收
    questions = Question.objects.order_by('-pub_date')
    # render将会找到模板文件，发送给用户
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    # question_id用于接收URL传来的参数
    question = Question.objects.get(id=question_id)
    # 字典的key将成为detail.html模板中的变量名，value成为变量的值
    return render(request, 'detail.html', {'question': question})

def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})

def vote(request, question_id):
    # 取出问题
    question = Question.objects.get(id=question_id)
    # 通过用户提交的表单，取出用户选择项目的id
    print(dir(request))   # 在终端上打印request所有属性
    print(request.POST)
    choice_id = request.POST.get('choice_id')
    # 通过问题的choice_set管理器取出选项实例
    choice = question.choice_set.get(id=choice_id)
    # 修改选项的票数
    choice.votes += 1
    choice.save()
    # 重定向到结果页
    return redirect('result', question.id)
