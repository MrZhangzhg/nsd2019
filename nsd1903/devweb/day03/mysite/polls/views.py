from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # django将会把http请求作为参数传递给函数，因此，函数必须至少有一个参数
    return HttpResponse('<h1>首页</h1>')
