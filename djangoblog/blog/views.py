from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'blog/index.html')


def post_listing(request):
    # get all the posts
    posts = Post.objects.all().filter(is_draft=False).order_by("-publication_date")[:10]
    return render(request, 'blog/post_listing.html', {'posts': posts})


def post_detail(request, pk):
    # get post
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        # render error template
        error_message = 'Invalid id {} for post.'.format(pk)
        return render(request, 'blog/error.html', {'error_message': error_message})

    # render template
    return render(request, 'blog/post_detail.html', {'post': post})