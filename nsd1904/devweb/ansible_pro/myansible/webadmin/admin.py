from django.contrib import admin
from .models import HostGroup, Host, Module, Argument

# Register your models here.
for item in [HostGroup, Host, Module, Argument]:
    admin.site.register(item)
