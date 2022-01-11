from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Appointment
from .forms import CommentForm, AvailabilityForm
from django.views.generic import ListView
from datetime import datetime
from django.core.mail import send_mail
from django.utils import timezone


def home_page(request):
    return render(request, 'index.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter().order_by('-created_on')
    template_name = 'content-list.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        return render(
            request,
            "content-detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "content-detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
            },
        )


class BookingView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "availability.html")

    def post(self, request, *args, **kwargs):
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form. cleaned_data

        now = data["start_time"]

        if now < timezone.now():
            return render(request, "unsuccessful.html")

        bookingList = Appointment.objects.filter(start__lt=data['end_time'], end__gt=data['start_time'])
        if not bookingList:
            booking = Appointment.objects.create(
                name=data["name"], 
                email=data["email"],
                start=data["start_time"],
                end=data["end_time"]
                )
            booking.save()
            name_user = data["name"]
            start_time = data["start_time"]
            end_time = data["end_time"]
            email_user = data["email"]
            send_mail("Virtual PT Session", f"Thanks {name_user} For Booking Your Appointment with us.\n" + 
            f"Please join the following zoom link on {start_time} \n" +
            " https://us04web.zoom.us/j/8339571591?pwd=dG9MQy9nUWN6a0F2dUo4L04rQkxPQT09",
            "engage.fitness.training.1@gmail.com", [email_user], fail_silently=True)
            return render(request, "success.html", {
                "booking":booking
            },)
        else:
            name = data["name"]
            return render(request, "booked.html",{
                "name":name, 
            },)








        
