from django.shortcuts import render
from .models import Question

# 用户的请求将自动作为第一个参数发给函数
# 所以函数至少需要有一个参数
def index(request):
    questions = Question.objects.order_by('-pub_date')
    # render函数寻找名为index.html的模板文件，返回给用户
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    # render的字符，将以key=val的形式发给模板文件
    # key在模板文件中用于变量名，val是变量的值
    return render(request, 'detail.html', {'question': question})

def result(request, question_id):
    return render(request, 'result.html', {'question_id': question_id})
