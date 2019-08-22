from django.shortcuts import render
from .models import Question

# Create your views here.

def index(request):
    # django将会把http请求作为参数传递给函数，因此，函数必须至少有一个参数
    # return HttpResponse('<h1>首页</h1>')
    # 取出所有问题，根据pub_date降序排列
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'detail.html', {'question': question})

def result(request, question_id):
    return render(request, 'result.html', {'question_id': question_id})
