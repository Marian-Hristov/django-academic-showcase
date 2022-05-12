from django.forms import ModelForm, ValidationError
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.post_id = kwargs.pop('post_id', None)
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs = {'placeholder': 'Comment here...', 'class': 'form-control', 'cols':'30', 'rows':'5'}
        self.fields['body'].label = 'Comment'

    def clean_body(self):
        data = self.cleaned_data['body']
        if len(data) > 500:
            raise ValidationError("Comment too long! Max of 500 characters")
        elif len(data) < 1:
            raise ValidationError("Comment too small! Min of 1 character")
        return data
    
    def return_data(self):
        return (self.cleaned_data['body'])