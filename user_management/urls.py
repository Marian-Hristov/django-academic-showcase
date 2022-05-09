from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_profile, name='register'),
    path('', views.LoginRedirectView.as_view(), name='redirect-to-login'),
    # path('register/', views.UserRegisterView.as_view(), name='register')z
]
