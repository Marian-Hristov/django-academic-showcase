from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.UserRegisterView.as_view(), name='register')
]