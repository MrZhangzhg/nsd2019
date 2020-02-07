from django.shortcuts import render
from .models import HostGroup

def index(request):
    return render(request, 'hosts.html')

def add_hosts(request):
    groups = HostGroup.objects.all()
    return render(request, 'add_hosts.html', {'groups': groups})
