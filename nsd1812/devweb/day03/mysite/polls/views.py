from django.shortcuts import render, redirect
from polls.models import Question

def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'detail.html', {'question': question})

def vote(request, question_id):
    # 取出问题
    question = Question.objects.get(id=question_id)
    if request.method == 'POST':
        # 取出用户的选择
        choice_id = request.POST.get('choice_id')
        # 取出选项实例
        choice = question.choice_set.get(id=choice_id)
        choice.votes += 1
        choice.save()

    # redirect相当于打开一个新窗口，访问网址。
    # 如果仍然采用render，将会把request的数据继续向result传递
    return redirect('result', question_id=question_id)

def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})
