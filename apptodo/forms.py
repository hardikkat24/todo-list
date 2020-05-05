from django import forms
from todo_api.models import Task, Group, GroupTask, Member
from django.contrib.auth.forms import UserCreationForm
from todo_api.models import MyUser, Task


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('email',)



class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('task', )


class GroupForm(forms.Form):
    """Not a model form as data to be added in two models"""
    group_name = forms.CharField(max_length=40)


class MemberAddForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ['user']


class TaskGroupTaskForm(forms.ModelForm):

    class Meta:
        model = GroupTask
        fields = ["task",]

