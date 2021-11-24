from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.PostList.as_view(), name='content'),
    path('booking_list/', views.AppointmentList.as_view(), name='AppointmentList'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='content-detail'),
]