from django.shortcuts import render

# Create your views here.
# 每个函数至少需要有一个参数，用于接收客户端发来的请求
def index(request):
    # render用于查找模板文件，并返回给用户
    return render(request, 'index.html')

def detail(request, question_id):
    # 字典的内容，将会被转义成key=val的形式，发送给detail.html
    return render(request, 'detail.html', {'question_id': question_id})

def result(request, question_id):
    return render(request, 'result.html', {'question_id': question_id})
