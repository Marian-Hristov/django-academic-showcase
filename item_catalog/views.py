from django.http import Http404, HttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from item_catalog.models import Post
from user_management.models import Profile

# Create your views here.

def likeView(request, pk, action):
    if request.method == "POST":
        post = get_object_or_404(Post, id=pk)
        user = get_object_or_404(Profile, user=request.user)
        if action == "disliked":
            post.likes.remove(user)
            post.save()
        elif action == "liked":
            post.likes.add(user)
            post.save()
        else:
            return HttpResponseServerError("Invalid action on post")
        return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))
    else:
        return Http404()

class PostDetailView(DetailView):
    model = Post
    template_name = 'item_catalog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(Profile, user=self.request.user)
        return context

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