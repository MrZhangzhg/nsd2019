from django.conf.urls import url
# from polls import views
from . import views

urlpatterns = [
    # 访问首页时，使用views.index函数响应，该url的名字是index
    url(r'^$', views.index, name='index'),
    # \d+匹配数字，为其添加()，匹配到的数字将会成detail的参数
    url(r'^(\d+)/$', views.detail, name='detail'),
    url(r'^(\d+)/result/$', views.result, name='result'),
    url(r'^(\d+)/vote/$', views.vote, name='vote'),
]
