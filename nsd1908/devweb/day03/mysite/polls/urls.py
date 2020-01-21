from django.conf.urls import url
# from polls import views  # 也可以写为以下形式
from . import views

urlpatterns = [
    # 从http://x.x.x.x/polls/后面开始匹配
    # 访问首页，将会调用views.index函数
    # 为http://x.x.x.x/polls/这个url起名为index
    url(r'^$', views.index, name='index'),
    # 注意正则中后面的/，务必写上
    # \d+匹配数字，用()括起来，它就会自动作为参数传给detail函数
    url(r'^(\d+)/$', views.detail, name='detail'),
    url(r'^(\d+)/result/$', views.result, name='result'),
]
