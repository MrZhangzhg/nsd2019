from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^addhosts/$', views.addhosts, name='addhosts'),
    url(r'^addmodules/$', views.addmodules, name='addmodules'),
    url(r'^delarg/(?P<arg_id>\d+)/$', views.delarg, name='delarg'),
    url(r'^tasks/$', views.tasks, name='tasks'),
]
