from django.shortcuts import render, HttpResponse

# Create your views here.

# 用户发给django的请求，函数必须提供一个参数进行接收
def index(request):
    # return HttpResponse('<h1>polls首页</h1>')
    return render(request, 'index.html')
