from multiprocessing import get_context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Profile, User, get_def_avatar
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from user_management.models import Profile
from .forms import ProfileCreationForm, PasswordResetForm
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
    return Profile.objects.all().filter(user_id=inp_user.id)

def dashboard(request):
    if request.user.is_authenticated:
        context = {'Profile': None, 'User': User.objects.all().filter(username=request.user).first()}
        if len(get_profile(context['User'])) == 0:
            new_profile = Profile(
                user = User.objects.all().filter(username=request.user).first()
            )
            new_profile.save()

            new_profile.avatar = bytes(new_profile.avatar).decode()

            context['Profile'] = new_profile
        else:
            profile = get_profile(context['User'])[0]
            profile.avatar = bytes(profile.avatar).decode()
            context['Profile'] = profile
        return render(request, 'user_management/dashboard.html', context=context)
    else:
        return render(request, 'user_management/dashboard.html')



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
            print(f.errors)
    else:
        f = ProfileCreationForm()
    return render(request, 'registration/register.html', {'form': f})

def reset_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user_management/reset_password.html', {
        'form': form
    })