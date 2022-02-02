from django.shortcuts import render

from project_products.models import Product


def product_list(request, *args, **kwargs):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context)


def product_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    products = Product.objects.get_by_id(selected_product_id)
    context = {
        'products': products
    }
    return render(request, 'product_detail.html', context)
