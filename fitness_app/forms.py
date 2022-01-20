from .models import Comment, Post
from django import forms
from django.forms import ModelForm
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import User
from django.forms import FileInput, CheckboxSelectMultiple, Select

class MakeWorkOutForm(forms.ModelForm):
    author = forms.ModelChoiceField(label="author", queryset=User.objects.all())

    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class AvailabilityForm(forms.Form):
    name = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=254, required=True)
    start_date = forms.DateTimeField(required=True,
                                     input_formats=['%Y-%m-%d%H:%M'])
    end_date = forms.DateTimeField(required=True,
                                   input_formats=['%Y-%m-%d%H:%M'])
    
    def clean_start_time(self):
        start = self.cleaned_data.get('start_date')
        if start < timezone.now():
            raise forms.ValidationError('the date must be after now.')

