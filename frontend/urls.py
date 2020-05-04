from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# API URLs
urlpatterns = [
    path('home/', views.home, name = "home"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('task-home/', views.task_home, name = "task-home"),
]


