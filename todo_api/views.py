from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .serializers import TasksSerializer
from django.core.exceptions import PermissionDenied
from apptodo.models import Tasks


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'task-list': '/task-list',
    }
    return Response(api_urls)


@login_required
@api_view(['GET'])
def apiTaskList(request):
    tasks = Tasks.objects.filter(username = request.user)
    serializer = TasksSerializer(tasks, many = True)
    return Response(serializer.data)


@login_required
@api_view(['GET'])
def apiTaskDetail(request, pk):
    task = Tasks.objects.get(pk = pk)
    if request.user == task.username:
        serializer = TasksSerializer(task, many = False)
        return Response(serializer.data)
    raise PermissionDenied
    return


@login_required
@api_view(['GET'])
def apiTaskDetail(request, pk):
    task = Tasks.objects.get(pk = pk)
    if request.user == task.username:
        serializer = TasksSerializer(task, many = False)
        return Response(serializer.data)
    raise PermissionDenied
    return


@login_required
@api_view(['POST'])
def apiTaskCreate(request):
    serializer = TasksSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(username = request.user)

    return Response(serializer.data)