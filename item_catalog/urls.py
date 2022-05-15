from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('post/create', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/detail', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/like/<str:action>', views.likeView, name="post-like"),
    path('projects/personal/<str:username>', views.ProjectListView.as_view(), name="projects"),
    path('projects/personal/<str:username>/project/<int:pk>', views.ProjectDetailView.as_view(), name="project-detail"),
    path('projects/create/<str:username>', views.ProjectCreateView.as_view(), name="project-create"),
    path('projects/personal/<str:username>/project/<int:pk>/update', views.ProjectUpdateView.as_view(), name="project-update"),
    path('projects/personal/<str:username>/project/<int:pk>/delete', views.ProjectDeleteView.as_view(), name="project-delete"),
    path('flag/post/<int:pk>', views.flag_post, name="flag-post"),
]