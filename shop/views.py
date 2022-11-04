from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Logo

def site_logo_edit(request):

    image = Logo.image.objects.all()
    
    return render(request, 'shop/base.html', context={'logo_main': image})


def product_list(request, category_slug=None):

    category = None
    categories = Category.objects.filter(parent=None)
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product/shop-sub-category-list.html',
                  context={'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):

    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    return render(request, 'shop/product/detail-02.html', context={'product': product})


