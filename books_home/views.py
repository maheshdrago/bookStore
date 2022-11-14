from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Books
from store.models import *



def index(request):

    
    if request.method=="POST":
        text = request.POST['search']
        all_books = Books.objects.filter(title__icontains=text)

        if not all_books:
            context = {
                'books':[],
                'flag':1,
                'mes':"No books found"
            }
            return render(request,"books_home/index.html",context=context)

    else:
        all_books = Books.objects.all()
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = 0

        for i in items:
            cartItems+=int(i.quantity)
    else:
        items = []
        cartItems=0
    
    context = {
            'books':all_books,
            'flag':0,
            'items':items,
            "cartItems":cartItems
            }

    return render(request,"books_home/index.html",context=context)

def about(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = 0

        for i in items:
            cartItems+=int(i.quantity)
    else:
        items = []
        cartItems=0
    context={
        'cartItems':cartItems
    }
    return render(request,'books_home/about.html',context=context)

def register(request):

    if request.method=="POST":
        
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username is already taken.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email already exists.")
                else:
                    user = User.objects.create_user(username=username,password=password1,email=email)
                    user.save()
                    """profile = Customer.objects.create(user=user,email=user.email,name=user.username)
                    profile.save()"""

                    messages.success(request,'You ar now registered')
                    return redirect('login')
                    
        else:
            
            messages.error(request,"Passwords do not match")
            return redirect('register')
    else:
        
        return render(request,"books_home/register.html")

    


def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user:
            
            auth.login(request,user)
            messages.success(request,"You are now logged in")
            profile, created = Customer.objects.get_or_create(user=request.user,email=request.user.email,name=request.user.username)
            return redirect("index")

        else:
            
            messages.error(request,"Invalid Credentials")
            return redirect('login')


    return render(request,'books_home/login.html')



def logout(request):

    
    auth.logout(request)
    messages.success(request,"Logged Out")
    return redirect('index')

def show_book(request,listing_id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = 0

        for i in items:
            cartItems+=int(i.quantity)
    else:
        items = []
        cartItems=0

    book = get_object_or_404(Books,pk=listing_id)

    context ={
        "book":book,
        'cartItems':cartItems
    }

    return render(request,'books_home/book.html',context=context)

def byCategory(request,category):

    if category!="all":
        books = Books.objects.filter(category=category)
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = 0

            for i in items:
                cartItems+=int(i.quantity)
        else:
            items = []
            cartItems=0
        
        if len(books)==0:

            context = {
                'books':[],
                'flag':1,
                'mes':"No books found",
                'items':items,
                "cartItems":cartItems
                }
        else:
            context = {
                    'books':books,
                    'flag':0,
                    'items':items,
                    "cartItems":cartItems
                    }
        
        return render(request,"books_home/index.html",context=context)
    else:
        return redirect('index')


    return HttpResponse(str(books))