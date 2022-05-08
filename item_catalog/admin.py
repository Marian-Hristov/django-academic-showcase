from django.contrib import admin
from item_catalog.models import Comment, Post, Project

# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ] 


admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)