from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .serializers import TaskSerializer
from django.core.exceptions import PermissionDenied
from .models import Task
from django.views.decorators.csrf import csrf_protect


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'task-list': '/task-list/',
        'task-detail': '/task-detail/pk/',
        'task-create': '/task-create/',
        'task-update': '/task-update/pk/',
        'task-delete': '/task-delete/pk/',

    }
    return Response(api_urls)


@login_required
@api_view(['GET'])
def apiTaskList(request):
    tasks = Task.objects.filter(user = request.user)
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)


@login_required
@api_view(['GET'])
def apiTaskDetail(request, pk):
    task = Task.objects.get(pk = pk)
    if request.user == task.user:
        serializer = TaskSerializer(task, many = False)
        return Response(serializer.data)
    raise PermissionDenied


@login_required
@api_view(['GET', 'POST'])
def apiTaskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user = request.user)

    return Response(serializer.data)


@login_required
@api_view(['POST'])
def apiTaskUpdate(request, pk):
    task = Task.objects.get(pk = pk)
    if task.user == request.user:
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    raise PermissionDenied


@login_required
@api_view(['DELETE'])
def apiTaskDelete(request, pk):
    task = Task.objects.get(pk = pk)
    if task.user == request.user:
        task.delete()
        return Response("Successfully Deleted!")
    raise PermissionDenied