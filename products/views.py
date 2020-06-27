from django.shortcuts import render
from .models import Products
# Create your views here.
def products(request):
    products = Products.objects.all()
    context = {
        'products' : products
    }
    url = 'products/products.html'
    return  render(request , url , context)