from django.urls import path
from .views import blogs_list, blog_detail

app_name = "blogs"

urlpatterns = [
    path('', blogs_list, name="blog_list"),
    path('blog-detail/<blogId>', blog_detail, name="blog_detail")
]
