from django.conf.urls import url
from . import views

urlpatterns = [
    # url(正则, 函数, name=该url的名字),
    url(r'^$', views.index, name='index'),
    url(r'^news/$', views.news, name='news'),
]
