from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='mainpage'),
    url(r'^add_hosts/$', views.add_hosts, name='add_hosts'),
]
