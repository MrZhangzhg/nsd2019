from django.conf.urls import url
from . import views   # 在当前目录(包)中导入views

urlpatterns = [
    # 当访问http://x.x.x.x/polls/时，使用views中的index函数进行处理
    # 给http://x.x.x.x/polls/这个url起个名叫index
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/$', views.detail, name='detail'),
    url(r'^(\d+)/result/$', views.result, name='result'),
    url(r'^(\d+)/vote/$', views.vote, name='vote'),
]
