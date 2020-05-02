from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.apiOverview, name = 'api-overview'),
    path('task-list/', views.apiTaskList, name = 'api-task-list'),
    path('task-detail/<int:pk>/', views.apiTaskDetail, name = 'api-task-detail'),
    path('task-create/', views.apiTaskCreate, name = 'api-task-create'),
    path('task-update/<int:pk>/', views.apiTaskUpdate, name = 'api-task-update'),
    path('task-delete/<int:pk>/', views.apiTaskDelete, name = 'api-task-delete'),
]