from django.shortcuts import render

# 每个函数至少需要一个参数，用于接收用户发来的请求
def index(request):
    return render(request, 'index.html')

def detail(request, question_id):
    # 字典的内容将转换成question_id=nn传给detail.html，作为它可以使用的变量
    return render(request, 'detail.html', {'question_id': question_id})
