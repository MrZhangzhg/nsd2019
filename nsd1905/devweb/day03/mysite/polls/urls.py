from django.conf.urls import url
# from polls import views
from . import views

urlpatterns = [
    # 访问首页时，使用views.index函数响应，该url的名字是index
    url(r'^$', views.index, name='index'),
]
