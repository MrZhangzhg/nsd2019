from django.conf.urls import url
# from polls import views   # 也可以用下面的形式
from . import views   # 从当前目录(包)导入views模块

urlpatterns = [
    # url从http://x.x.x.x/polls/后面开始匹配
    # 访问投票首页时，使用views.index函数响应
    # 为该url(http://x.x.x.x/polls/)起名为index
    url(r'^$', views.index, name='index'),
    # 将\d+用()括起来，它匹配的内容，将会作为detail的参数
    url(r'^(\d+)/$', views.detail, name='detail'),
    url(r'^(\d+)/result/$', views.result, name='result'),
    url(r'^(\d+)/vote/$', views.vote, name='vote'),
]
