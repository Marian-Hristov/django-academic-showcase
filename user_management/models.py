from django.db import models
from django.contrib.auth.models import User
import base64
import os

# class 

# Create your models here.
def get_def_avatar():
    with open('academic_showcase/default_images/avtr.jpg', "rb") as img_file:
        return base64.b64encode(img_file.read())

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.BinaryField(default=get_def_avatar)

    def __str__(self):
        return str(self.name)
