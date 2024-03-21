from django.shortcuts import render
from .utils import cartData, guestOrder
from store.models import Customer, Order, ShippingAddress
from django.http import JsonResponse, HttpResponse
import json
import datetime
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# @login_required
def checkout(request):
    try:
        userObj = User.objects.get(id=request.user.id)
        customer_all_add = userObj.customer.shipping_address.all().order_by('-id')
        customer_add = customer_all_add.first()
    except:
        userObj = False
        customer_all_add = []
        customer_add = {}
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'customer_add': customer_add,
               'customer_all_add': customer_all_add, 'userObj': userObj}
    return render(request, 'checkout.html', context)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
        except:
            return HttpResponse('There is no linked customer')
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
           shipping_address, created = ShippingAddress.objects.get_or_create(
            customer=customer,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )
    else:
        guestOrder(request, data)
    return JsonResponse('Payment submitted..', safe=False)


def getAddress_ajax(request):
    id = request.GET.get('id')
    obj = ShippingAddress.objects.get(id=id)
    data = {
        'address': obj.address,
        'city': obj.city,
        'state': obj.state,
        'zipcode': obj.zipcode,
    }
    return JsonResponse(data, safe=False)
