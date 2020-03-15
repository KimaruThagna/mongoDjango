from django.urls import path
from . views import *
urlpatterns = [
    path('posts/', AllPosts.as_view(), name='all_posts'),
]
