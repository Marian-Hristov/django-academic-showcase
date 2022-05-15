from re import template
from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import Group, User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.contenttypes.models import ContentType
from item_catalog.models import Post

from user_management.forms import ProfileCreationForm
from user_management.models import Profile
from web_admin.forms import AddProfileToGroupForm

def index(request):
    return render_dashboard(request, "Members")

@permission_required(perm=['auth.administrate_members'], login_url="/user_management/login",)
def toggle_block(request, user_id: str):
    # grp: Group = Group.objects.get(name="Member")
    user_obj = User.objects.get(username=user_id)
    # user_in_set: User = grp.user_set.get(id=user_id)
    if user_obj:
        try:
            permission = user_obj.user_permissions.get(codename='can_interact')
            user_obj.user_permissions.remove(permission)
        except Permission.DoesNotExist: 
            ct = ContentType.objects.get_for_model(Profile)
            permission = Permission.objects.get(content_type=ct, codename='can_interact')
            user_obj.user_permissions.add(permission)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        
    else:
        return HttpResponseNotFound()

@permission_required(perm=['auth.administrate_members'], login_url="/user_management/login")
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
        'form': AddProfileToGroupForm(profiles=profiles_not_in_group),
    }

    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render(context, request))

@permission_required(perm=['auth.administrate_members'], login_url="/user_management/login", raise_exception=True)
def create_profile(request):
    if request.method == 'POST':
        f = ProfileCreationForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return HttpResponse('<script type="text/javascript">window.close()</script>')  
        else:
            print(f.errors)
    else:
        f = ProfileCreationForm()
    template = loader.get_template('popup.html')
    return HttpResponse(template.render({'form': f}, request))

@permission_required(perm=['item_catalog.administrate_projects'], login_url="/user_management/login", raise_exception=True)
def flagged_view(request):
    flagged_posts = Post.objects.filter(flagged=True)
    template = loader.get_template('flagged_posts.html')
    return HttpResponse(template.render({'posts': flagged_posts}, request))

@permission_required(perm=['item_catalog.administrate_projects'], login_url="/user_management/login", raise_exception=True)
def unflag_post(request, post_id):
    post: Post = Post.objects.get(id=post_id)
    post.flagged = False
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def del_from_group(request, group_name, username):
    user: User = User.objects.get(username=username)
    Group.objects.get(name=group_name).user_set.remove(user)
    print(user.groups.count())
    if user.groups.count() == 0:
        user.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))