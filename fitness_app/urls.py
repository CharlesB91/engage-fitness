from . import views
from django.urls import path

urlpatterns = [
    path('content/', views.PostList.as_view(), name='content'),
]