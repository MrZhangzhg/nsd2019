from django.shortcuts import render
from .models import Group

# Create your views here.

def index(request):
    return render(request, 'webadmin/server_info.html')

def add_hosts(request):
    groups = Group.objects.all()
    return render(request, 'webadmin/add_hosts.html', {'groups': groups})

