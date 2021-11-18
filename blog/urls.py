from django.urls import path

from .views import render_posts, render_post

app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='posts'),
    path('<int:post_id>', render_post, name='post'),
]
