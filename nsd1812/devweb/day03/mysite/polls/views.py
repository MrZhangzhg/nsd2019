from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def detail(request, question_id):
    return render(request, 'detail.html', {'qid': question_id})

def result(request, question_id):
    return render(request, 'result.html', {'qid': question_id})
