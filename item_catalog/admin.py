from django.contrib import admin
from item_catalog.models import Comment, Post, Project, Rating

# Register your models here.
admin.site.register(Project)
admin.site.register(Comment)
# admin.site.register(Post, PostAdmin)
admin.site.register(Post)
admin.site.register(Rating)