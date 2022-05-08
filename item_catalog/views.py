from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from item_catalog.models import Post

# Create your views here.

class PostDetailView(DetailView):
    model = Post
    template_name = 'item_catalog/post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    template_name = "item_catalog/post_update.html"

def index(request):
    items = Post.objects.filter()
    template = loader.get_template('item_catalog/home.html')
    context = {
        'posts': items
    }
    return HttpResponse(template.render(context, request))