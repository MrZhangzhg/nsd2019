from django.contrib import admin
from .models import Question, Choice  # 在当前目录的models中导入模型

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
