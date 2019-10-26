from django.shortcuts import render

# Create your views here.
def index(request):
    # 用户发起请求，请求的内容将会作为函数的第一个参数，所以函数至少需要有一个参数
    return render(request, 'index.html')

def detail(request, question_id):
    # question_id用于接收url传过来的参数
    # 字典将传递给detail.html，detail.html将其作为变量使用，字典的key
    # 是变量名，字典的value是变量值
    return render(request, 'detail.html', {'question_id': question_id})
