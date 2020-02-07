from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='mainpage'),
    url(r'^add_hosts/$', views.add_hosts, name='add_hosts'),
    url(r'^add_modules/$', views.add_modules, name='add_modules'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^del_arg/(\d+)/$', views.del_arg, name='del_arg'),
]
