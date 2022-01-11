from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AvailabilityForm(forms.Form):
    name = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=254, required=True)
    start_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    end_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])

