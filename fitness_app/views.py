from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import generic, View
from .models import Post, Appointment
from .forms import CommentForm, AvailabilityForm, MakeWorkOutForm, EditWorkOutForm
from django.views.generic import ListView
from django.core.mail import send_mail
from django.utils import timezone
from cloudinary.forms import cl_init_js_callbacks


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

class createWorkOut(View):
    
    def get(self, request, *args, **kwargs):

        form = MakeWorkOutForm()
        context = {"form": form}
        return render(request, "add-workout.html", context)

    def post(self, request, *args, **kwargs):

        form = MakeWorkOutForm()
        if request.method == "POST":
            form = MakeWorkOutForm(request.POST)
            if form.is_valid():
                form.save()

        return render(request, "add-workout.html")


class EditWorkOut(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.get(slug=slug)
        form = EditWorkOutForm(instance=queryset)
        context = {'form': form}
        
        return render(request, "edit-workout.html", context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.get(slug=slug)
        form = EditWorkOutForm(instance=queryset)
        if request.method == "POST":
            form = EditWorkOutForm(request.POST, instance=queryset)
            if form.is_valid():
                form.save()

        return render(request, "edit-workout.html")

class DeleteWorkOut(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.get(slug=slug)

        return render(request, "delete.html")

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.get(slug=slug)
        if request.method == "POST":
            queryset.delete()
            return HttpResponse("Deleted")

        return render(request, "delete.html")



class BookingView(View):

    def get(self, request, *args, **kwargs):

        return render(request, "availability.html")

    def post(self, request, *args, **kwargs):
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form. cleaned_data
            print(timezone.now())
        else:
            return render(request, "unsuccessful.html")

        bookingList = Appointment.objects.filter(start_date__lt=data
                                                 ['end_date'],
                                                 end_date__gt=data
                                                 ['start_date'])

        if not bookingList:
            booking = Appointment.objects.create(
                name=data["name"],
                email=data["email"],
                start_date=data["start_date"],
                end_date=data["end_date"],
                )
            booking.save()
            name_user = data["name"]
            start_email = data["start_date"]
            email_user = data["email"]
            send_mail("Virtual PT Session", f"Thanks {name_user} For Booking" +
                      "Your Appointment with us.\n" +
                      "Please join the following zoom link on" +
                      f"{start_email}\n" +
                      "https://us04web.zoom.us/j/8339571591?pwd=" +
                      "dG9MQy9nUWN6a0F2dUo4L04rQkxPQT09",
                      "engage.fitness.training.1@gmail.com", [email_user],
                      fail_silently=False)
            return render(request, "success.html", {
                "booking": booking
            },)
        else:
            name = data["name"]
            return render(request, "booked.html", {
                "name": name,
            },)
