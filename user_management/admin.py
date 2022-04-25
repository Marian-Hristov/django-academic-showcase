from tkinter import Image
from django.contrib import admin
from user_management.models import Profile, ImageFile

# Register your models here.
admin.site.register(Profile)
admin.site.register(ImageFile)
