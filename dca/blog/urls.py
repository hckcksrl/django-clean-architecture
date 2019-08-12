from django.urls import path
from .views.view import Post

urlpatterns = [
    path('<int:post_id>',Post.as_view() , name='post')
]
