from django.shortcuts import render, redirect
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
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})

def vote(request, question_id):
    # 取出问题
    question = Question.objects.get(id=question_id)
    # request是一个对象，它的POST属性是一个字典，字典中存储着表单数据
    choice_id = request.POST.get('choice_id')
    # 获取choice_id对应的选项实例
    choice = question.choice_set.get(id=choice_id)
    # 将选项的票数加1
    choice.votes += 1
    choice.save()
    # 投票完成后，跳转到投票结果页
    return redirect('result', question.id)
