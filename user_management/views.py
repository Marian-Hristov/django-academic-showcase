from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import ProfileCreationForm
from django.contrib import messages
# Create your views here.

def dashboard(request):
    return render(request, "user_management/dashboard.html")

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name =  'registration/register.html'
    success_url = reverse_lazy('login')

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
