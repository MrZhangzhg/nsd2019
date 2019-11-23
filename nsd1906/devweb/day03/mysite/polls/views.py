from django.shortcuts import render
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
    return render(request, 'result.html', {'question_id': question_id})

