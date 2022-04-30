from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from django.views.generic.detail import DetailView

from item_catalog.models import Post

# Create your views here.

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.get_comments()
    template = loader.get_template('item_catalog/post.html')
    context = {
        'post': post,
        # 'comments': comments
    }
    return HttpResponse(template.render(context, request))

def index(request):
    items = Post.objects.filter()
    template = loader.get_template('item_catalog/home.html')
    context = {
        'posts': items
    }
    return HttpResponse(template.render(context, request))