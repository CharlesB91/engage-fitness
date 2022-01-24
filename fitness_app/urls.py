from . import views
from django.urls import path


urlpatterns = [
    path('content-list/', views.PostList.as_view(), name='content-list'),
    path('add-workout/', views.createWorkOut.as_view(), name='add-workout'),
    path('availability/', views.BookingView.as_view(), name='availability'),
    path('success/', views.BookingView.as_view(), name='success'),
    path('unsuccessful/', views.BookingView.as_view(), name='unsuccessful'),
    path('booked/', views.BookingView.as_view(), name='booked'),
    path('edit-workout/<slug:slug>', views.EditWorkOut.as_view(), name='edit-workout'),
    path('delete/<slug:slug>', views.DeleteWorkOut.as_view(), name='delete-workout'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='content-detail'),
]