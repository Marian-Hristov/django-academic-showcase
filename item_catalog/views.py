from xml.etree.ElementTree import Comment
from django.http import Http404, HttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from item_catalog.forms import CommentForm

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


class PostComment(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = 'item_catalog/post_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.user = get_object_or_404(Profile, user=self.request.user)
        comment.body = form.return_data()
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('post_detail', kwargs={'pk': post.pk})

class PostDetailView(DetailView):
    model = Post
    template_name = 'item_catalog/post_detail.html'
    context_object_name = 'post'
    redirect_authenticated_user = True
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('redirect-to-login'))
        return super(DetailView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('redirect-to-login'))
        else:
            self.object = self.get_object()
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                context = self.get_context_data()
                new_comment.user = context['profile']
                new_comment.post = get_object_or_404(Post, id=self.kwargs['pk'])
                new_comment.save()
        return super(DetailView, self).get(request, *args, **kwargs)

    def process_request(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('redirect-to-login'))
        return None 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile'] = get_object_or_404(Profile, user=self.request.user)
            context['form'] = CommentForm()
        return context


class PostUpdateView(UpdateView):
    model = Post
    template_name = "item_catalog/post_update.html"

    fields = [
        "title",
        "project",
    ]

    redirect_authenticated_user = True

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('redirect-to-login'))
        return super(UpdateView, self).get(request, *args, **kwargs)

    def process_request(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('redirect-to-login'))
        return None 

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("post-detail", kwargs={"pk": pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = "item_catalog/post_delete.html"
    success_url = reverse_lazy('item_catalog')
    redirect_authenticated_user = True

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('redirect-to-login'))
        return super(DeleteView, self).get(request, *args, **kwargs)

    def process_request(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('redirect-to-login'))
        return None 


def index(request):
    items = Post.objects.filter()
    template = loader.get_template('item_catalog/home.html')
    context = {
        'posts': items
    }
    return HttpResponse(template.render(context, request))