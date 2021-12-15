from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import generic, View
from .models import Post, Appointment
from .forms import CommentForm, AvailabilityForm
from django.views.generic import ListView, FormView
import datetime


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

class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = "availability.html"

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        bookingList = Appointment.objects.filter(start__lt= data['end_time'], end__gt= data['start_time'])
        print(bookingList)

        if not bookingList:
            booking=Appointment.objects.create(
                name=data["name"], 
                start=data["start_time"],
                end=data["end_time"]
                )
            booking.save()
            print(booking.start)
            print(data["start_time"])
            return HttpResponse("can be booked")
            return HttpResponse("cant be booked")
        else:
            return HttpResponse("cant be booked")
        
        # for booking in bookingList:
        #     if booking.start__gt == data['start_time']:
        #         booking=Appointment.objects.create(
        #             name=data["name"], 
        #             start=data["start_time"],
        #             end=data["end_time"]
        #             )
        #         booking.save()
        #         print(booking.start)
        #         print(data["start_time"])
        #         return HttpResponse("can be booked")
        #     else:
        #         print(booking.start )
        #         print(data["start_time"])
        #         return HttpResponse("Cant be booked")





        
