from django.shortcuts import render

# Create your views here.
def index(request):
    # 用户发起请求，请求的内容将会作为函数的第一个参数，所以函数至少需要有一个参数
    return render(request, 'index.html')

