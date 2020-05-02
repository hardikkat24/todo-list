from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    email = models.EmailField(max_length=256, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Task(models.Model):
    """Stores tasks of users"""
    task = models.CharField(max_length=200, blank=False)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null = False)
    posted_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default = False, blank = False)

    def __str__(self):
        return self.task


class Group(models.Model):
    """Stores information of TaskGroups"""
    group_name = models.CharField(max_length = 40, blank = False)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, null = False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name


class Member(models.Model):
    """Stores pairs of Group and User whenever a User is added"""
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null = False)
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE, null = False)

    class Meta:
        unique_together = ('user', 'group_name')

    def __str__(self):
        return str(self.user) + " in " + str(self.group_name)


class GroupTask(models.Model):
    """Stores tasks of TaskGroups"""
    task = models.CharField(max_length=200, blank=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null = False)
    added_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=False)
    added_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, blank=False)