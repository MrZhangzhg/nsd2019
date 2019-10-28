from django.shortcuts import render, redirect
from .models import Question

# Create your views here.
def index(request):
    # 用户发起请求，请求的内容将会作为函数的第一个参数，所以函数至少需要有一个参数
    # 取出所有的问题，根据发布时间进行降序排列
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    # question_id用于接收url传过来的参数
    # 字典将传递给detail.html，detail.html将其作为变量使用，字典的key
    # 是变量名，字典的value是变量值
    question = Question.objects.get(id=question_id)
    return render(request, 'detail.html', {'question': question})

def result(request, question_id):
    # 取出问题，发往模板
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    # 当用户提交表单时，request.POST是一个字典，里面记录了与POST相关的数据
    # choice_id是detail.html页面中单选按钮的name，值是选项的id
    choice_id = request.POST.get('choice_id')
    choice = question.choice_set.get(id=choice_id)
    choice.votes += 1
    choice.save()

    # 这里返回使用的不是render，因为render直接返回页面，URL不变，也就是
    # http://x.x.x.x/polls/2/vote显示的是2号问题的投票结果，这是不合理的
    # 应该由http://x.x.x.x/polls/2/result/显示投票结果。所以使用redirect
    return redirect('result', question_id)
