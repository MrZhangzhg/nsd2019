from django.contrib import admin
# 在当前目录下的models模块中导入模型
from .models import Question, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
