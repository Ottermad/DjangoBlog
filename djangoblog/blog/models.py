from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(unique=True, max_length=30)
    body = models.TextField()
    author = models.ForeignKey(User)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    body = models.CharField(max_length=300)
