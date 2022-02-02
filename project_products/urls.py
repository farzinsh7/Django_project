from django.urls import path
from .views import product_detail, product_list

app_name = "products"

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product-detail/<productId>', product_detail, name='product_detail'),
]
