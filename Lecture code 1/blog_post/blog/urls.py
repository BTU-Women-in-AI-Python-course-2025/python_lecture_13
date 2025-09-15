from django.urls import path
from blog.views import create_blog_post, thank_you

urlpatterns = [
    path('create_blog_post/', create_blog_post, name='create_blog_post'),
    path('thank_you/', thank_you, name='thank_you'),

]
