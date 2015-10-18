from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'blog/index.html')


def posts_listing(request):
    # get all the posts
    posts = Post.objects.all().filter(is_draft=False).order_by("-publication_date")[:10]
    return render(request, 'blog/post_listing.html', {'posts': posts})
