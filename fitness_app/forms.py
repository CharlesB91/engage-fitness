from .models import Comment, Post
from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget


# Create Workout Form

class MakeWorkOutForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ("featured_image",)
        fields = "__all__"
        widgets = {
            'content': SummernoteWidget(),
        }


# Edit Workout Form

class EditWorkOutForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ("featured_image",)
        fields = "__all__"
        widgets = {
            'content': SummernoteWidget(),
        }


# Comment Form

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)


# Appointment Booking Form

class AvailabilityForm(forms.Form):

    name = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=254, required=True)
    start_date = forms.DateTimeField(required=True,
                                     input_formats=['%Y-%m-%d%H:%M'])
    end_date = forms.DateTimeField(required=True,
                                   input_formats=['%Y-%m-%d%H:%M'])