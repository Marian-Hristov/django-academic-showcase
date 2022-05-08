from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from item_catalog.models import Post

# Create your views here.

# def LikeView(request, pk, action):
#     post = get_object_or_404(Post, id=request.POST.request.get('post-id'))
#     if action == "disliked":
#         post.likes.add(request.user)
#     else:
#         post.likes.remove(request.user)
#     return HttpResponseRedirect(reverse('post-detail', args=[str(pk),action]))

class PostDetailView(DetailView):
    model = Post
    template_name = 'item_catalog/post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    template_name = "item_catalog/post_update.html"

    fields = [
        "title",
        "project",
    ]

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("post-detail", kwargs={"pk": pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = "item_catalog/post_delete.html"
    success_url = reverse_lazy('item_catalog')


def index(request):
    items = Post.objects.filter()
    template = loader.get_template('item_catalog/home.html')
    context = {
        'posts': items
    }
    return HttpResponse(template.render(context, request))