from django import forms
from user_management.models import Profile

PROFILES = [tuple([user.user.username, user.user.username]) for user in Profile.objects.all()]

class MessagingForm(forms.Form):
    body = forms.Textarea()
    recipients = forms.CharField(label="Message Recipient: ", 
    widget=forms.Select(choices=PROFILES))