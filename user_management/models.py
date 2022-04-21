from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# class 

# Create your models here.

class ImageFile(models.Model):
    image = models.FileField()
    image_data = models.BinaryField(null=True)

class Profile(AbstractBaseUser):
    name = models.CharField(max_length=254)
    email_addr = models.EmailField(max_length=254)
    avatar = ImageFile()


