from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('signup/', views.signup, name = "signup"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name = "logout"),
    path('addtask/', views.addtask, name = "addtask"),
    path('delete/<int:pk>/', views.delete_task, name = "delete"),
    path('complete/<int:pk>/', views.complete_task, name="complete"),
    path('creategroup/', views.creategroup, name = "creategroup"),
    path('group/<int:pk>/', views.group, name = "grouppage"),
    path('group/<int:pk>/add/', views.group_member_add, name = "groupmemberadd"),
    path('group/<int:id>/delete/<int:pk>/', views.delete_grouptask, name = "delete_grouptask"),
    path('group/<int:id>/complete/<int:pk>/', views.complete_grouptask, name="complete_grouptask"),
]