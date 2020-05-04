from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, TaskForm
from django.contrib import messages
from django.views.generic import FormView
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    return render(request, "home.html")


def signup(request):
    """Registers new user"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Account successfully created")
            return redirect('login')

    form = CustomUserCreationForm()
    context = {
        'form': form,
    }

    return render(request, "signup.html", context)


def task_home(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, "task_home.html", context)