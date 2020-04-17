from django.db import models
from django.contrib.auth.models import User
# import json


class Tasks(models.Model):
    """Stores tasks of users"""
    task = models.CharField(max_length=200, blank=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null = False)
    posted_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default = False, blank = False)

    def __str__(self):
        return self.task


class TaskGroupList(models.Model):
    """Stores information of TaskGroups"""
    group_name = models.CharField(max_length = 40, blank = False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null = False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name

    """
    members = models.TextField()

    def set_members(self, x):
        "Converts list of members into string to be saved in members field"
        self.members = json.dumps(x)

    def get_members(self):
        "Converts data stored in members field to list of members"
        return json.loads(self.members)

    """


class UserGroup(models.Model):
    """Stores pairs of Group and User whenever a User is added"""
    member = models.ForeignKey(User, on_delete=models.CASCADE, null = False)
    group_name = models.ForeignKey(TaskGroupList, on_delete=models.CASCADE, null = False)

    class Meta:
        unique_together = ('member', 'group_name')

    def __str__(self):
        return str(self.member) + " in " + str(self.group_name)


class TaskGroupTask(models.Model):
    """Stores tasks of TaskGroups"""
    task = models.CharField(max_length=200, blank=False)
    group = models.ForeignKey(TaskGroupList, on_delete=models.CASCADE, null = False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    added_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, blank=False)
