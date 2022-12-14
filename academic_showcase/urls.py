"""academic_showcase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

import item_catalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item_catalog/', include('item_catalog.urls'), name='posts'),
    path('', include('django.contrib.auth.urls'), name='login'),
    path('user_management/', include('user_management.urls'), name='dashboard'),
    path('web_admin/', include('web_admin.urls'), name='web_admin'),
    path('user_management/', include('django.contrib.auth.urls')),
    path('message/', include('user_messaging.urls')),
    path('', item_catalog.views.PostListView.as_view(), name='index')
]