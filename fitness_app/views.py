from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter().order_by('-created_on')
    template_name = 'content-list.html'
    paginate_by = 6

def home_page(request):
    return render(request, 'index.html')
