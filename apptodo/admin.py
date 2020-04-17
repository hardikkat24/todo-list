from django.contrib import admin
from .models import Tasks, TaskGroupList, UserGroup, TaskGroupTask


# Register your models here.

admin.site.register(Tasks)
admin.site.register(TaskGroupList)
admin.site.register(UserGroup)
admin.site.register(TaskGroupTask)