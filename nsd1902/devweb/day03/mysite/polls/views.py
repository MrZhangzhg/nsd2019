from django.shortcuts import render, HttpResponse, redirect
from .models import Question

# Create your views here.

# 用户发给django的请求，函数必须提供一个参数进行接收
def index(request):
    # return HttpResponse('<h1>polls首页</h1>')
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'detail.html', {'question': question})

def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    choice_id = request.POST.get('choice_id')  # 从用户post的表单中取出choice_id
    choice = question.choice_set.get(id=choice_id)  # 获取选项实例
    choice.votes += 1
    choice.save()

    return redirect('result', question_id)  # 重定向到result页面
