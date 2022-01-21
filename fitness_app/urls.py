from . import views
from django.urls import path
# from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('home/', views.PostList.as_view(), name='content'),
    path('add-workout/', views.createWorkOut.as_view(), name='add-workout'),
    path('availability/', views.BookingView.as_view(), name='availability'),
    path('success/', views.BookingView.as_view(), name='success'),
    path('unsuccessful/', views.BookingView.as_view(), name='unsuccessful'),
    path('booked/', views.BookingView.as_view(), name='booked'),
    path('<slug:slug>', views.EditWorkOut.as_view(), name='edit-workout'),
    path('done/', views.EditWorkOut.as_view(), name='done'),
    path('done/', views.createWorkOut.as_view(), name='done'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='content-detail'),
]