from django.conf.urls import url
from . import views   # 从当前目录中导入views模块

urlpatterns = [
    # url(路径正则, 调用的函数, 该url的名字)
    url(r'^$', views.index, name='index'),
]
