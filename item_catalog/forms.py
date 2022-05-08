from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean_body(self):
        data = self.cleaned_data['body']
        if len(data) > 500:
            raise ValidationError("Comment too long! Max of 500")
        return data