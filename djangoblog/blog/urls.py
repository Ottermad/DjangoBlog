from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^posts/', views.post_listing, name='post_listing'),
    url(r'^$', views.index, name='index')
]
