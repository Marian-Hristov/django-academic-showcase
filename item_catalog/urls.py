from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='item_catalog'),
    path('post/<int:pk>/detail', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    # path('post/<int:pk>/like/<str:action>', views.LikeView, name="post-like"),
]