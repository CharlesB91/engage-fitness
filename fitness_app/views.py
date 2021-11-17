from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class ContentList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'content-list.html'
    paginate_by = 6
