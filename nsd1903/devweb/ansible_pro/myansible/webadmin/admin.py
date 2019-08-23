from django.contrib import admin
from .models import Group, Host, Module, Args

# Register your models here.

for item in [Group, Host, Module, Args]:
    admin.site.register(item)
