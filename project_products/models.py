from django.db import models
from django.db.models import Q


def upload_image_path(instance, filename):
    final_name = f"{instance.id}-{instance.title}"
    return f"products/{final_name}"


class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(in_stock=True)

    def get_product_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to=upload_image_path)
    price = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now_add=True, auto_now=False)
    in_stock = models.BooleanField(default=False)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField("Tag", blank=True, null=True)

    objects = ProductsManager()

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
