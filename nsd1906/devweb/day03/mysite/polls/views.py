from django.shortcuts import render, redirect
from .models import Question

# Create your views here.
def index(request):
    # 用户发起的请求将会作为第一个参数传给函数
    # 所以函数至少要定义一个参数来接收用户的请求
    questions = Question.objects.order_by('-pub_date')
    # render负责找寻模板文件发送给用户
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    # 在数据库中取出具体的问题
    question = Question.objects.get(id=question_id)
    # 字典的内容将会成为模板文件的变量，字典的key是变量名，val是变量值
    return render(request, 'detail.html', {'question': question})

def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})

def vote(request, question_id):
    # 取出问题
    question = Question.objects.get(id=question_id)
    # request是用户的请求，它有很多属性，客户端提交的数据保存到了
    # request.POST字典中，choice_id是表单的属性
    choice_id = request.POST.get('choice_id')
    # 通过问题取出选项实例
    choice = question.choice_set.get(id=choice_id)
    # 将选项的votes属性值加1
    choice.votes += 1
    choice.save()
    # 投票结束后，跳转到投票结果页
    return redirect('result', question.id)
