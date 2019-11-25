from django.contrib import admin
from .models import HostGroup, Host, Module, Args

# Register your models here.
for item in [HostGroup, Host, Module, Args]:
    admin.site.register(item)
