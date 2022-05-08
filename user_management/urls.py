from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_profile, name='register'),
    path('reset_password/', views.reset_pass, name='reset_password')
    # path('register/', views.UserRegisterView.as_view(), name='register')z
]
