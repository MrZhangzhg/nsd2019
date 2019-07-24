from django.shortcuts import render, HttpResponse
from .models import Question

# Create your views here.

# 用户发给django的请求，函数必须提供一个参数进行接收
def index(request):
    # return HttpResponse('<h1>polls首页</h1>')
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    return render(request, 'detail.html', {'question_id': question_id})

def result(request, question_id):
    return render(request, 'result.html', {'question_id': question_id})
