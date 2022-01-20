from . import views
from django.urls import path
# from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('home/', views.PostList.as_view(), name='content'),
    path('add-workout/', views.createWorkOut, name='add-workout'),
    path('availability/', views.BookingView.as_view(), name='availability'),
    path('success/', views.BookingView.as_view(), name='success'),
    path('unsuccessful/', views.BookingView.as_view(), name='unsuccessful'),
    path('booked/', views.BookingView.as_view(), name='booked'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='content-detail'),
]