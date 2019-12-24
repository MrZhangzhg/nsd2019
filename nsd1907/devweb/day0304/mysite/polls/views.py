from django.shortcuts import render

# 用户的请求将自动作为第一个参数发给函数
# 所以函数至少需要有一个参数
def index(request):
    # render函数寻找名为index.html的模板文件，返回给用户
    return render(request, 'index.html')

