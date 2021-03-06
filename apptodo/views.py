from django.shortcuts import render, redirect
from todo_api.models import Task, GroupTask, Group, Member
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import TaskForm, GroupForm, MemberAddForm, TaskGroupTaskForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()


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


@login_required
def addtask(request):
    """Displays and adds task to task list of a user"""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            messages.success(request, "Task added successfully")
        else:
            messages.error(request, "failed")

    form = TaskForm()
    context = {
        'form' : form,

    }
    return render(request, 'taskpage.html', context )


@login_required
def delete_task(request, pk):
    """Deletes task from task list of a user"""
    task = Task.objects.get(pk = pk)

    task.delete()
    return redirect('addtask')


@login_required
def complete_task(request ,pk):
    """Marks task as done"""
    task = Task.objects.get(pk = pk)

    task.status = True
    task.save()
    return redirect('addtask')


@login_required
def creategroup(request):
    """Creates a TaskGroup"""
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['group_name']
            group = Group(group_name = name, created_by = request.user)
            group.save()
            usergroup = Member(user = request.user, group_name = group)
            usergroup.save()

    form = GroupForm()
    context = {
        'form': form,
    }
    return render(request, "create_group.html", context)


@login_required
def allgroups(request):
    groups = Member.objects.filter(user = request.user)
    context = {
        "groups": groups,
    }
    return render(request, "allgroups.html", context)

@login_required
def group_member_add(request, pk):
    """Adds member to a TaskGroup"""
    group1 = Group.objects.get(pk = pk)

    if request.method == "POST":
        form = MemberAddForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.group_name = group1
            post.save()
            messages.success(request, "Added!", fail_silently=True)
        else:
            messages.error(request, "not added!")

    form = MemberAddForm()

    context = {
        "group_list": group1,
        "form": form,
    }

    return render(request, "group_member_add.html", context)


@login_required
def group(request, pk):
    """Displays and add tasks of TaskGrouo"""
    groupx = Group.objects.get(pk = pk)
    if request.method == "POST":
        form = TaskGroupTaskForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.added_by = request.user
            post.group = groupx
            post.save()
            messages.success(request, "Task added successfully")
        else:
            messages.error(request, "failed")

    form = TaskGroupTaskForm()
    context = {
        'form' : form,
        'group': groupx,
    }
    return render(request, 'group_page.html', context )


@login_required
def delete_grouptask(request, id, pk):
    """Deletes task from TaskGroup"""
    task = GroupTask.objects.get(pk = pk)
    task.delete()
    return redirect('grouppage', pk = id)


@login_required
def complete_grouptask(request, id, pk):
    """Marks task as complete from TaskGroup"""
    task = GroupTask.objects.get(pk = pk)

    task.status = True
    task.save()
    return redirect('grouppage', pk = id)

