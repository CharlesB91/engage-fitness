from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.PostList.as_view(), name='content'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='content-detail'),
]