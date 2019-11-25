from django.shortcuts import render
from .models import HostGroup

# Create your views here.
def index(request):
    return render(request, 'webadmin.html')

def add_hosts(request):
    groups = HostGroup.objects.all()
    return render(request, 'add_hosts.html', {'groups': groups})
