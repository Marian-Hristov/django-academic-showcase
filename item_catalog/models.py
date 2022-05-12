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
    name = models.CharField(max_length=30) # placeholder so i can use profile

    def __str__(self) -> str:
        return self.name


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

    def __str__(self) -> str:
        return self.name

    class Meta:
        permissions = [
            ('administrate_projects', 'Can administrate project')
        ]


class Post(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,validators=[empty_string_validation])
    likes = models.ManyToManyField(Profile, related_name="post_like")

    def get_number_of_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField(max_length=500,null=False,blank=False,validators=[empty_string_validation])
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self) -> str:
        return f"Comment from {self.user} at {self.creation_date}: {self.body[0:5]}..." 

    def get_comments(self):
        return Comment.objects.filter(parent=self)


# class Commentable(models.Model):

#     # returns an list of comment_sections
#     def get_children(self):
#         return None #TODO get children where id is equal to this objects id, (Marian, 04-26)
#                         # TODO maybe this should be in views? (Marian, 04-26)


# class CommentSection(Commentable):
#     parent = models.ForeignKey(Commentable, on_delete=models.CASCADE, related_name='+')

#     # validation for parent type
#     def validate_parent(parent):
#         if isinstance(Commentable): # TODO: do we need this? (Marian, 04-27)
#             return True
#         return False

#     def __init__(self, parent):
#         if self.validate_parent(parent):
#             self.parent = parent
#         else:
#             raise TypeError("Accepted parent of CommentSection type: Post, CommentSection")

#     # returns the parent, either post or comment_section
#     def get_parent(self):
#         return self.parent


# class Comment(models.Model):
#     creation_date = models.DateField(auto_now_add=True)
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     body = models.CharField(max_length=300)
#     parent = models.ForeignKey(CommentSection, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return f"Comment from {self.user} at {self.creation_date}: {self.body[0:5]}..." 
