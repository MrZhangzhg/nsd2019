from django.shortcuts import render

# Create your views here.

def webadmin_index(request):
    return render(request, 'webadmin_index.html')

def add_hosts(request):
    return render(request, 'addhosts.html')
