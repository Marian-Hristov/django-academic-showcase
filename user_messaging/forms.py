from user_management.models import Profile
from django import forms
from django.core.exceptions import ValidationError



def get_profiles():
    try:
        print([tuple([prof.user.username, prof.user.username]) for prof in Profile.objects.all()]) 
        return [tuple([prof.user.username, prof.user.username]) for prof in Profile.objects.all()]
    except:
        return [('No Profiles', 'No Profiles')]

class MessagingForm(forms.Form):
    body = forms.CharField(label="Enter Text: ", widget=forms.Textarea())
    recipients = forms.CharField(label="Message Recipient: ",
    widget=forms.Select(choices=get_profiles()))

    def get_data(self):
        return self.cleaned_data.get('body'), self.cleaned_data.get('recipients')


