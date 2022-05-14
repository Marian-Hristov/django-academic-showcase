from django.urls import path
from .import views

urlpatterns = [
    path('send_message/', views.send_message),
    path('view_messages', views.view_messages)
] 