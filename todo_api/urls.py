from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.apiOverview, name = 'api-overview'),
    path('task-list/', views.apiTaskList, name = 'api-task-list'),
    path('task-detail/<int:pk>/', views.apiTaskDetail, name = 'api-task-detail'),
]