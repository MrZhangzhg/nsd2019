from django.shortcuts import render

# Create your views here.
# 每个函数至少需要有一个参数，用于接收客户端发来的请求
def index(request):
    # render用于查找模板文件，并返回给用户
    return render(request, 'index.html')

