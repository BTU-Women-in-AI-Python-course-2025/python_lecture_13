from django.urls import path
from blog.views import create_blog_post, success_page_blog_post_created

urlpatterns = [
    path('create_blog_post/', create_blog_post, name='create_blog_post'),
    path('success_page_blog_post_created', success_page_blog_post_created, name='success_page_blog_post_created')

]
