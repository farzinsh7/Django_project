from django.shortcuts import render

from project_blogs.models import Blog, Tag, Category


def blogs_list(request):
    blogs = Blog.objects.get_active_blogs()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs.html', context)


def blog_detail(request, *args, **kwargs):
    selected_blog_id = kwargs['blogId']
    blog = Blog.objects.get_by_id(selected_blog_id)
    tags = Tag.objects.filter(blog=blog)
    category = Category.objects.all()
    recent_post = Blog.objects.all().order_by("-publish_at")[:3]
    context = {
        'blog': blog,
        'tags': tags,
        'category': category,
        'recent': recent_post,
    }
    return render(request, 'blogs_detail.html', context)
