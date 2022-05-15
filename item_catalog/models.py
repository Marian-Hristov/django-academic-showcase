from django.db import models
from django.forms import ValidationError
from user_management.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator

import os
import base64

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


# Function to get image
def get_def_proj_avatar():
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'academic_showcase/default_images/project_avtr.png'), "rb") as img_file:
        return base64.b64encode(img_file.read())


class Rating(models.Model):
    rating_value = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False)


class Project(models.Model):
    name = models.CharField(max_length=75)
    project_type = models.CharField(max_length=40)
    field = models.CharField(max_length=50)
    keywords = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=20)
    image = models.BinaryField(default=get_def_proj_avatar,null=False,blank=False)
    creation_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=one_week_hence,validators=[due_date_validation])
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        permissions = [
            ('administrate_projects', 'Can administrate project')
        ]


class Post(models.Model):

    def __get_zero():
        return [0]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    ratings = models.ManyToManyField(Rating, related_name="post_rating", default=__get_zero(), blank=True)
    title = models.CharField(max_length=100,validators=[empty_string_validation])
    flagged = models.BooleanField(default=False)
    likes = models.ManyToManyField(Profile, related_name="post_like", default=__get_zero(), blank=True,)

    def __str__(self) -> str:
        return self.title

    def get_number_of_likes(self):
        return self.likes.count()

    def get_avrg_rating(self):
        return self.ratings.aggregate(models.Avg("rating_value"))
    
    def user_has_liked(self, user):
        return self.likes.all()


class Comment(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField(max_length=500,null=False,blank=False,validators=[empty_string_validation])
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self) -> str:
        return f"Comment from {self.user} at {self.creation_date}: {self.body[0:5]}..." 

    def get_comments(self):
        return Comment.objects.filter(parent=self)