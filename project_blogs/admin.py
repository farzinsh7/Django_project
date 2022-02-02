from django.contrib import admin

from project_blogs.models import Blog, Category, Tag

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
