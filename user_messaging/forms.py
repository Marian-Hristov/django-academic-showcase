from user_management.models import Profile
from django import forms
from django.core.exceptions import ValidationError

PROFILES = [tuple([prof.user.username, prof.user.username]) for prof in Profile.objects.all()]

class MessagingForm(forms.Form):
    body = forms.CharField(label="Enter Text: ", widget=forms.Textarea())
    recipients = forms.CharField(label="Message Recipient: ",
    widget=forms.Select(choices=PROFILES))

    def get_data(self):
        return self.cleaned_data.get('body'), self.cleaned_data.get('recipients')


