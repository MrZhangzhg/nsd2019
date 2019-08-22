from django.conf.urls import url
from . import views   # 从当前目录中导入views模块

urlpatterns = [
    # url(路径正则, 调用的函数, 该url的名字)
    url(r'^$', views.index, name='index'),
    # (\d+)将会把匹配到的数字作为参数传递给detail函数
    url(r'^(\d+)/$', views.detail, name='detail'),
    url(r'^(\d+)/result/$', views.result, name='result'),
    url(r'^(\d+)/vote/$', views.vote, name='vote'),
]
