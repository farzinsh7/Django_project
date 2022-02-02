from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models import Q


class BlogManager(models.Manager):
    def get_active_blogs(self):
        return self.get_queryset().filter(show=True)

    def get_blog_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, show=True)

    def get_by_id(self, blog_id):
        qs = self.get_queryset().filter(id=blog_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tags__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, show=True).distinct()


def upload_image_path(instance, filename):
    final_name = f"{instance.id}-{instance.title}"
    return f"blogs/{instance.title}/{final_name}"


class Blog(models.Model):
    title = models.CharField(max_length=150)
    slug_field = models.SlugField(default='slug')
    description = models.TextField(default='description')
    image = models.ImageField(upload_to=upload_image_path, null=True)
    content = RichTextField(null=True)
    seo_meta = models.TextField(default='seo meta')
    keywords = models.CharField(max_length=200, null=True)
    show = models.BooleanField(default=False)
    publish_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True, related_name='blog')
    tags = models.ManyToManyField("Tag", blank=True, null=True, related_name='blog')
    # comments =

    objects = BlogManager()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=True, null=True)
    published_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=True, null=True)
    published_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.title
