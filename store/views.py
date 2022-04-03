from django.shortcuts import get_object_or_404, render
from store.models import Product
from category.models import Category

def store(request, category_slug = None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category = categories, is_available = True)
        productCount = products.count()

    else:

        products = Product.objects.all().filter(is_available = True)
        productCount = products.count()
    contex = {
        'products':products,
        'productCount':productCount,
    }
    return render(request, 'store/store.html',contex)

def product_details(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product':single_product,
    }
    return render(request, 'store/product_detail.html', context)