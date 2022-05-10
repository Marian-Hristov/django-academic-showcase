from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import Group, User

from user_management.models import Profile

# Create your views here.

def index(request):
    return render_dashboard(request, "Members")

def render_dashboard(request, group_name):
    template = loader.get_template('dashboard.html')
    selected_group = Group.objects.get(name=group_name)
    
    profiles = []
    for profile in Profile.objects.all():
        if profile.user in selected_group.user_set.all():
            profiles.append(profile)
            profile.avatar = bytes(profile.avatar).decode()

    context = {
        "groups": Group.objects.all(),
        "selected_group": selected_group,
        "profiles": profiles,
    }
    return HttpResponse(template.render(context, request))


def del_from_group(request, group_name, username):
    Group.objects.get(name=group_name).user_set.remove(User.objects.get(username=username))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
