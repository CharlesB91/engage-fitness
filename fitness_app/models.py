from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

# Models Table

class Post(models.Model):
    # Title of work out with max length 200 which is a unique tile so its cant be used again
    title = models.CharField(max_length=200, unique=True)
    # Slug field is used to determine the URL
    slug = models.SlugField(max_length=200, unique=True)
    # This is the author field who posted the workout. This is a ForeignKey as it relates to an other database table
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workout_posts")
    # Date workout was updated which defaults to the current date
    updated_on = models.DateTimeField(auto_now=True)
    # Workout illustration image which will be stored to cloudinary
    featured_image = CloudinaryField('image', default='placeholder')
    # This creates an index for the page
    excerpt = models.TextField(blank=True)
    # This indicates what date the workout was created on
    created_on = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        # ordered created on field starting with newest first
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"



