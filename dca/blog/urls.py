from django.urls import path
from .views.view import Post,Blog

urlpatterns = [
    path('post/', Blog.as_view(), name='blog'),
    path('<int:post_id>',Post.as_view() , name='post'),
]
