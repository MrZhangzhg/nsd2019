from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hosts.html')

def add_hosts(request):
    return render(request, 'add_hosts.html')
