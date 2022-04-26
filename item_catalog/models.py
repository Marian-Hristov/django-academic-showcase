from operator import mod
from tkinter import CASCADE
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

class Profile(models.Model):
    name = models.CharField() # placeholder so i can profile

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
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=False, blank=False)
    # image = models.BinaryField(blan=True, null=True, editable=True)

    def __str__(self) -> str:
        return self.name


class CommentSection(models.Model):
    __comments = models.ManyToManyField() # TODO one to many field
    parent = None

    def validate_parent(parent):
        if isinstance(parent, CommentSection) or isinstance(parent, Post):
            return True
        return False

    def __init__(self, parent):
        if self.validate_parent(parent):
            self.parent = parent
        else:
            raise TypeError("Accepted parent of CommentSection type: Post, CommentSection")

    # returns an list of comment_sections
    def get_children(self):
        return None

    # returns a list of comments
    def get_comments(self):
        return self.comments

    # returns the parent, either post or comment_section
    def get_parent(self):
        return self.parent


class Comment(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    parent = models.ForeignKey(CommentSection, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Comment from {self.user} at {self.creation_date}: {self.body[0:5]}..." 


class Post(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,validators=[empty_string_validation])
    flagged = models.BooleanField()
    comment_section = models.ManyToOneRel()  # TODO: one to many field
