from django.shortcuts import redirect, render
from blog.forms import BlogPostForm
from blog.models import BlogPost


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            BlogPost.objects.create(**form.cleaned_data)
            return redirect('thank_you')
    else:
        form = BlogPostForm()
    return render(request, template_name='create_blog_post.html', context={'form': form})


def thank_you(request):
    return render(request, template_name='thank_you.html')
