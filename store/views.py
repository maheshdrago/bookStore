from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from .models import Order,OrderItem
from books_home.models import Books



# Create your views here.

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = 0
        total_price = 0

        for i in items:
            cartItems+=int(i.quantity)
        
        for i in items:
            total_price+=(i.quantity*i.book.price)
    else:
        items = []
        cartItems=0
        total_price = 0
    
    context = {'items':items,'cartItems':cartItems,"total_price":total_price}

    return render(request,'store/cart.html',context=context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = 0
        total_price = 0

        for i in items:
            cartItems+=int(i.quantity)
        
        for i in items:
            total_price+=(i.quantity*i.book.price)

    else:
        items = []
        cartItems=0
        total_price = 0
    
    context = {
        'total_price':total_price,
        'cartItems':cartItems,
        'items':items
    }
    return render(request,'store/checkout.html',context=context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    book = Books.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order,book=book)

    if action=="add":
        orderItem.quantity +=1
        
    else:
        orderItem.quantity-=1
        
    orderItem.save()

    if orderItem.quantity<=0:
        orderItem.delete()
    
    
    return JsonResponse("item was added",safe=False)

def thanks(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

        for item in items:
            item.delete()
            
        cartItems = 0
        total_price = 0
        for i in items:
            cartItems+=int(i.quantity)
        
        for i in items:
            total_price+=(i.quantity*i.book.price)

    else:
        items = []
        total_price = 0
    
    context = {
        'total_price':total_price,
        'cartItems':cartItems,
        'items':items
    }
    
    return render(request,'store/thanks.html',context=context)

def credit(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems=0
        total_price = 0
        
        for i in items:
            cartItems+=int(i.quantity)
        
        for i in items:
            total_price+=(i.quantity*i.book.price)

    else:
        items = []
        total_price = 0
    
    context = {
        'total_price':total_price,
        'cartItems':cartItems
        
    }
    return render(request,'store/credit.html',context=context)


