from django.shortcuts import render
from .models import Product

# Create your views here.

def products_list(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    print(products)
    return render(request, 'products/products.html', context)
