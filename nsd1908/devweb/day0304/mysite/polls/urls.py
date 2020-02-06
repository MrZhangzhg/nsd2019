from django.conf.urls import url
from . import views  # 从当前目录导入views模块

urlpatterns = [
    # 用户访问http://x.x.x.x/polls/时，使用index函数响应，为该url起名为index
    url(r'^$', views.index, name='index'),
    # 将url中的数字用\d+匹配，再通过()将其作为参数传递给detail函数
    url(r'^(\d+)/$', views.detail, name='detail'),
    url(r'^(\d+)/result/$', views.result, name='result'),
    url(r'^(\d+)/vote/$', views.vote, name='vote'),
]
