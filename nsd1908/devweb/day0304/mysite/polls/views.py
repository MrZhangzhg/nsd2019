from django.shortcuts import render, redirect
from .models import Question

# 每个函数至少需要一个参数，用于接收用户发来的请求
def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'detail.html', {'question': question})
    # 字典的内容将转换成question_id=nn传给detail.html，作为它可以使用的变量
    # return render(request, 'detail.html', {'question_id': question_id})

def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})

def vote(request, question_id):
    # request是用户发来的请求，它是一个对象，其中它的POST属性是字典形式，对应表单post数据
    choice_id = request.POST.get('choice_id')
    question = Question.objects.get(id=question_id)  # 取出问题
    if choice_id:  # 如果choice_id非空
        choice = question.choice_set.get(id=choice_id)  # 通过问题取出选项
        choice.votes += 1
        choice.save()

    # 投票完成后跳转到投票结果页
    return redirect('result', question.id)
