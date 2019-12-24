from django.conf.urls import url
# from polls import views  # 也可以写为以下形式
from . import views


urlpatterns = [
    # 从http://x.x.x.x/polls/后面匹配
    # 用户访问polls首页时，将会调用views.index函数
    # 给http://x.x.x.x/polls/起名，叫index
    url(r'^$', views.index, name='index')
]
