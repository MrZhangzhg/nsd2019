from django.shortcuts import render

# Create your views here.
def index(request):
    # 用户的请求将会作为第一个参数传给函数，需要使用变量接收
    # render将会找到模板文件，发送给用户
    return render(request, 'index.html')

