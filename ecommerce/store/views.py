from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)



