
from . import views
from django.urls import path

urlpatterns = [
    path('hello/', views.hello_somebody, name='hello'),
    path('posts/', views.blog_all, name='posts'),
]