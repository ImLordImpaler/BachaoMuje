from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [

    path('' , views.cart , name ='cart'),
    path('update-cart' , views.update_cart , name='update_cart')
]
