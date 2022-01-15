from .models import Comment
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from dateutil import parser
from django.contrib.admin.widgets import AdminSplitDateTime


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class AvailabilityForm(forms.Form):
    name = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=254, required=True)
    start_date = forms.DateTimeField(required=True, input_formats=['%Y-%m-%d%H:%M'])
    end_date = forms.DateTimeField(required=True, input_formats=['%Y-%m-%d%H:%M'])

