from django.contrib import admin
# from polls.models import Question, Choice  # 也可以写为
from .models import Question, Choice  # 从当前目录的modes模块中导入

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)

