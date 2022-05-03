from multiprocessing import get_context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Profile, User

from user_management.models import Profile
from .forms import ProfileCreationForm
from django.contrib import messages
from django.views.generic import TemplateView
# Create your views here.

# class Dashboard(TemplateView):
#     template_name = 'user_management/dashboard.html'

#     def get_contfext_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(self.user.username)s
#         return context

def get_profile(inp_user):
    print(Profile.objects.all().filter(user_id=inp_user.id))
    return Profile.objects.all().filter(user_id=inp_user.id)

def dashboard(request):
    context = {'Profile': None, 'User': User.objects.all().filter(username=request.user).first()}
    print(context['User'])
    if len(get_profile(context['User'])) == 0:
        pass
    else:
        profile = get_profile(context['User'])[0]
        profile.avatar = bytes(profile.avatar).decode()
        context['Profile'] = profile
    return render(request, 'user_management/dashboard.html', context=context)



# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')

def register_profile(request):
    if request.method == 'POST':
        f = ProfileCreationForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            messages.success(request, 'Profile created successfully')
            return redirect('login')
    else:
        f = ProfileCreationForm()
    return render(request, 'registration/register.html', {'form': f})
