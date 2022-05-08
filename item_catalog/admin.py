from django.contrib import admin

from item_catalog.models import Comment, Post, Project

# Register your models here.
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Post)