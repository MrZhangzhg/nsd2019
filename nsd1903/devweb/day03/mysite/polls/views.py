from django.shortcuts import render, redirect
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

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    # request是用户的请求，POST是请求中的字典，保存着提交数据
    choice_id = request.POST.get('choice_id')
    # 通过问题的选项集取出对应的选项实例
    choice = question.choice_set.get(id=choice_id)
    choice.votes += 1  # 选项票数加1
    choice.save()

    # 使用重定向，url将会变成result的url，如果仍然使用render
    # 那么url显示的是vote，但是页面是result的页面
    return redirect('result', question_id)


def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})
