from django.shortcuts import render, redirect
from blog.forms import BlogPostForm, BlogPostModelForm
from blog.models import BlogPost


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            BlogPost.objects.create(**form.cleaned_data)
            return redirect('success_page_blog_post_created')
    else:
        form = BlogPostForm()

    return render(request, template_name='create_blog_post.html', context={'form': form})


def success_page_blog_post_created(request):
    return render(request, template_name='success_page_blog_post_created.html')


def create_blog_post_model_form(request):
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page_blog_post_created')
    else:
        form = BlogPostModelForm()

    return render(request, template_name='create_blog_post_model_form.html', context={'form': form})