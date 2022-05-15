
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('remove_from_group/<group_name>:<username>', views.del_from_group, name='del'),
    path('flagged_posts', views.flagged_view, name='flagged_posts'),
    path('block/<user_id>', views.toggle_block, name='toggle_block'),
    path('unflag_post/<post_id>', views.unflag_post, name='unflag_post'),
    path('profile_creation', views.create_profile, name='create_profile_popup'),
    path('<group_name>', views.render_dashboard, name='render_dashboard'),
]