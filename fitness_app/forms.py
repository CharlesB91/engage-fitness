from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class AvailabilityForm(forms.Form):
    start_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    end_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])

