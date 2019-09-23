from django.shortcuts import render
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
    return render(request, 'result.html', {'question_id': question_id})

