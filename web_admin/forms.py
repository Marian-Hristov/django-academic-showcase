import profile
from django import forms

from user_management.models import Profile

class AddProfileToGroupForm(forms.Form):
    profile_select = forms.ModelChoiceField(queryset=Profile.objects.none())
    profile_query = None

    def __init__(self, *args, **kwargs):
        try:
            profiles = kwargs.pop('profiles')
            super(AddProfileToGroupForm, self).__init__(*args, **kwargs)
            profiles = [p.user for p in profiles]
            query = Profile.objects.filter(user__in=profiles)
            AddProfileToGroupForm.profile_query = query
            self.fields['profile_select'].queryset = query
        except KeyError:
            print(AddProfileToGroupForm.profile_query)
            super(AddProfileToGroupForm, self).__init__(*args, **kwargs)
            self.fields['profile_select'].queryset = AddProfileToGroupForm.profile_query

