from django.urls import path

from .views import render_posts, render_post

urlpatterns = [
    path('', render_posts, name='posts'),
    path('<int:post_id>', render_post, name='post'),
]
