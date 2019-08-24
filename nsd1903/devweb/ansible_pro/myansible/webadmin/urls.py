from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='webadmin_index'),
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),
    url(r'^addmodules/$', views.add_modules, name='add_modules'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^(\d+)/del/$', views.del_args, name='del_args'),
]
