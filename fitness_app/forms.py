from .models import Comment
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AvailabilityForm(forms.Form):
    name = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=254, required=True)
    start_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    end_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])

    def clean_start_time(self):
        start = self.cleaned_data.get('start_time')
        if start < timezone.now():
            raise forms.ValidationError('the date must be after now.')
        return start


