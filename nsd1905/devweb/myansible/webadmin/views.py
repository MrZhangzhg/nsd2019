from django.shortcuts import render
from .models import HostGroup

# Create your views here.
def index(request):
    return render(request, 'webadmin.html')

def add_hosts(request):
    # print(request.method)   # 在终端打印请求方法
    # print(dir(request))  # 在终端中打印request的属性
    print(request.GET)
    print(request.POST)
    groups = HostGroup.objects.all()

    return render(request, 'add_hosts.html', {'groups': groups})
