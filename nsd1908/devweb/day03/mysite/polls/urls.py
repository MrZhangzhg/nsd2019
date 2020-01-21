from django.conf.urls import url
# from polls import views  # 也可以写为以下形式
from . import views

urlpatterns = [
    # 从http://x.x.x.x/polls/后面开始匹配
    # 访问首页，将会调用views.index函数
    # 为http://x.x.x.x/polls/这个url起名为index
    url(r'^$', views.index, name='index'),
]
