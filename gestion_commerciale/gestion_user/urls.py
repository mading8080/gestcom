from django.contrib.auth.views import LoginView, LogoutView
from .views import register
from django.urls import path
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
