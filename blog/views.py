from django.shortcuts import render
from .models import Post

# Create your views here.
def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def render_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts.html', {'post': post})