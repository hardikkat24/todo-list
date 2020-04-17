from django import forms
from .models import Tasks, TaskGroupList, UserGroup, TaskGroupTask


class TaskForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = ('task', )


class GroupForm(forms.Form):
    """Not a model form as data to be added in two models"""
    group_name = forms.CharField(max_length=40)


class MemberAddForm(forms.ModelForm):

    class Meta:
        model = UserGroup
        fields = ['member']


class TaskGroupTaskForm(forms.ModelForm):

    class Meta:
        model = TaskGroupTask
        fields = ["task",]

