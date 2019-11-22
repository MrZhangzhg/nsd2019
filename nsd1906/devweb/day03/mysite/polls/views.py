from django.shortcuts import render

# Create your views here.
def index(request):
    # 用户发起的请求将会作为第一个参数传给函数
    # 所以函数至少要定义一个参数来接收用户的请求
    # render负责找寻模板文件发送给用户
    return render(request, 'index.html')


