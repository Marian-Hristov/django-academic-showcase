from operator import mod
from django.db import models
from django.forms import ValidationError

# Create your models here.

# Validation functions
def one_week_hence():
        from django.utils import timezone
        return timezone.now() + timezone.timedelta(weeks=8)

def due_date_validation(due_date):
    from django.core.exceptions import ValidationError
    from django.utils import timezone
    if due_date < timezone.now().date(): 
        raise ValidationError("Due date cannot be set as before today")

def empty_string_validation(string: str):
    if len(string) < 1:
        raise ValidationError("Post title cannot be empty")

class ImageFile(models.Model):
    image = models.FileField()
    image_data = models.BinaryField(null=True,blank=True)

class Project(models.Model):
    name = models.CharField(max_length=75)
    type = models.CharField(max_length=40)
    field = models.CharField(max_length=50)
    keywords = models.CharField(max_length=500) # is there a way to have an array of keywords?
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=20)
    image = models.ForeignKey(ImageFile, null=True, blank=True,on_delete=models.DO_NOTHING)
    creation_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=one_week_hence,validators=[due_date_validation])
    
    # adding start and due date?
    # image = models.BinaryField(blan=True, null=True, editable=True)

    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    # user = models.ForeignKey(User) TODO make sure link is made (Marian Apr-21)

class Post(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,validators=[empty_string_validation])
    flagged = models.BooleanField()
