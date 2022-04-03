from django.shortcuts import get_object_or_404, render
from store.models import Product
from category.models import Category

def store(request, slug = None):
    categories = None
    products = None
    if slug != None:
        categories = get_object_or_404(Category, slug=slug)
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
