from django.conf.urls import url
# from polls import views  # 也可以写为以下形式
from . import views


urlpatterns = [
    # 从http://x.x.x.x/polls/后面匹配
    # 用户访问polls首页时，将会调用views.index函数
    # 给http://x.x.x.x/polls/起名，叫index
    url(r'^$', views.index, name='index'),
    # $前面的/务必填写，它可以匹配http://x.x.x.x/polls/1，
    # 也可以匹配 http://x.x.x.x/polls/1/
    # 为\d+添加()，将会把\d+匹配到的内容，传递给detail作为参数
    url(r'^(\d+)/$', views.detail, name='detail'),
    url(r'^(\d+)/result/$', views.result, name='result'),
    url(r'^(\d+)/vote/$', views.vote, name='vote'),
]
