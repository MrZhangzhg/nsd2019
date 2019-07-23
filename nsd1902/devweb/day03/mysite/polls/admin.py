from django.contrib import admin
from .models import Question, Choice  # 在当前目录中的models模块导入

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
