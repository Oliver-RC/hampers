from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """
    products = Product.objects.all().filter(is_available=True).order_by('-sku_created')

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
