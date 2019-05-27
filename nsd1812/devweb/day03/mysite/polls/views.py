from django.shortcuts import render
from polls.models import Question

def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    return render(request, 'detail.html', {'qid': question_id})

def result(request, question_id):
    return render(request, 'result.html', {'qid': question_id})
