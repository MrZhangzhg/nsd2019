from django.conf.urls import url
from . import views

urlpatterns = [
    # url(正则, 函数, name=该url的名字),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>\d+)/result/$', views.result, name='result'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
]
