from django.shortcuts import render
from .models import Cart
# Create your views here.
def cart(request):
    cart = Cart.objects.all()
    print(cart)
    context = {
        'cart': cart,
    }
    return render(request , 'cart/cart.html' , context)

def update_cart(request):
    pass