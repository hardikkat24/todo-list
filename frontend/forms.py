from django.contrib.auth.forms import UserCreationForm
from todo_api.models import MyUser, Task
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('email',)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('task', )
        widgets = {
            'task': forms.TextInput(attrs= {
                'id': 'post-task',
            })
        }