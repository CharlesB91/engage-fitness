from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.PostList.as_view(), name='content'),
    path('availability/', views.BookingView.as_view(), name='availability'),
    path('success/', views.BookingView.as_view(), name='success'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='content-detail'),
]