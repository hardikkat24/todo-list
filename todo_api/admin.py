from django.contrib import admin
from .models import Task, Group, GroupTask, Member, MyUser

# Register your models here.
admin.site.register(MyUser)

admin.site.register(Task)
admin.site.register(Group)
admin.site.register(GroupTask)
admin.site.register(Member)