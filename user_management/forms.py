from django.contrib.auth.models import User, Permission, Group
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from .models import Profile
import base64

class ProfileCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    first_name = forms.CharField(label='Enter your first name', min_length=1, max_length=150)
    last_name  = forms.CharField(label='Enter your last name', min_length=1, max_length=150)
    avatar = forms.ImageField(label='Choose an image for avatar (Ignore if you would like to set a default image)')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Input password's do not match!")

        return password2

    def save(self, commit=True):
        new_user = User.objects.create_user(
            username = self.cleaned_data.get('username'),
            email = self.cleaned_data.get('email'),
            password = self.cleaned_data.get('password1')
        )

        new_user.first_name = self.cleaned_data.get('first_name')
        new_user.last_name = self.cleaned_data.get('last_name')

        avtr_data = base64.b64encode(self.cleaned_data['avatar'].read())

        profile = Profile(user=new_user, avatar=avtr_data)
        ct = ContentType.objects.get_for_model(Profile)
        permission = Permission.objects.get(content_type=ct, codename='can_interact')
        new_user.user_permissions.add(permission)


        members, _ = Group.objects.get_or_create(name='Members')
        new_user.save()
        profile.save()

        if members:
            members.user_set.add(new_user)
        return profile


class PasswordResetForm(forms.Form):
    exist_pass = forms.CharField(label='Enter existing password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Enter new password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm new password', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Input password's do not match!")

        return password2
    
    def get_pass(self):
        return (self.cleaned_data.get('exist_pass'), self.cleaned_data.get('password2'))