from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, permission_required

from user_management.models import Profile
from web_admin.forms import AddProfileToGroupForm

# Create your views here.

def index(request):
    return render_dashboard(request, "Members")

@permission_required(perm=['auth.administrate_members'], login_url="/user_management/login", raise_exception=True)
def render_dashboard(request, group_name):
    canAdministrateAllUsers = request.user.has_perm('auth.administrate_users')

    selected_group: Group = Group.objects.get(name=group_name)
    groups = Group.objects.none()
    groups |= Group.objects.filter(name=group_name)

    if canAdministrateAllUsers:
        groups = Group.objects.all()
    else:
        if selected_group.name != 'Members':
            return HttpResponseForbidden()


    if request.method == "POST":
        form = AddProfileToGroupForm(request.POST)
        if form.is_valid():
            profile: Profile = form.cleaned_data['profile_select']
            selected_group.user_set.add(profile.user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    profiles = []
    profiles_not_in_group = []

    for profile in Profile.objects.all():
        if profile.user in selected_group.user_set.all():
            profiles.append(profile)
            profile.avatar = bytes(profile.avatar).decode()
        else:
            profiles_not_in_group.append(profile)


    context = {
        "groups": groups,
        "selected_group": selected_group,
        "profiles": profiles,
        "profiles_not_in_group": profiles_not_in_group,
        'form': AddProfileToGroupForm(profiles=profiles_not_in_group)
    }

    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render(context, request))

def del_from_group(request, group_name, username):
    Group.objects.get(name=group_name).user_set.remove(User.objects.get(username=username))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
