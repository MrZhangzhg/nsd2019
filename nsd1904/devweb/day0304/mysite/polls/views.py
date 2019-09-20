from django.shortcuts import render

# Create your views here.
def index(request):
    # 用户的请求将会作为第一个参数传给函数，需要使用变量接收
    # render将会找到模板文件，发送给用户
    return render(request, 'index.html')

def detail(request, question_id):
    # question_id用于接收URL传来的参数
    # 字典的key将成为detail.html模板中的变量名，value成为变量的值
    return render(request, 'detail.html', {'question_id': question_id})

def result(request, question_id):
    return render(request, 'result.html', {'question_id': question_id})

