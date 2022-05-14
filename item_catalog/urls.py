from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('post/create', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/detail', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/like/<str:action>', views.likeView, name="post-like"),
    path('projects/personal/<str:username>', views.ProjectListView.as_view(), name="projects"),
    path('projects/personal/<str:username>/project/<int:pk>', views.ProjectListView.as_view(), name="project-detail"),
    path('projects/create/<str:username>', views.ProjectCreateView.as_view(), name="project-create"),
]