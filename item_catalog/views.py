from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from item_catalog.models import Post

# Create your views here.
def index(request):
    items = Post.objects.filter()
    template = loader.get_template('item_catalog/home.html')
    context = {
        'posts': items
    }
    return HttpResponse(template.render(context, request))