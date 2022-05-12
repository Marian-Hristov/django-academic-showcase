from django.db import models
from user_management.models import Profile
# Create your models here.

class Message(models.Model):
    body = models.TextField()
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender_users")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver_users")
    send_date = models.DateTimeField(auto_now_add=True)