
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('remove_from_group/<group_name>:<username>', views.del_from_group, name='del'),
    path('<group_name>', views.render_dashboard, name='render_dashboard')
]