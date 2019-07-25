from django.shortcuts import render
from .models import HostGroup

# Create your views here.

def webadmin_index(request):
    return render(request, 'webadmin_index.html')

def add_hosts(request):
    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})
