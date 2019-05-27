from django.contrib import admin
from webansi.models import HostGroup, Host, Module, Argument

for item in [HostGroup, Host, Module, Argument]:
    admin.site.register(item)
