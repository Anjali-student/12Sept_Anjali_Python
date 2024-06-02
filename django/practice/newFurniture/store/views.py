from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login as authlogin
from django.contrib.auth import logout,login,authenticate
from django.core.mail import send_mail
from newFurniture import settings
from django.http import JsonResponse
import json
import datetime
from .utlis import cookieCart,cartData,guestOrder
from django.views.decorators.csrf import csrf_exempt





# Create your views here.
def main(request):
    user= request.user

    return render(request,'store/main.html',{'user':user})
		
def store1(request):
    data =cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    products = Product.objects.all()
    context = {'products':products,'cartItems':cartItems}
    return render(request, 'store/store.html',context)

def cart(request):
    data =cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
        
    context = {'items':items,'cartItems':cartItems,'order':order}
    return render(request, 'store/cart.html',context)

@csrf_exempt
def checkout(request):
    data =cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

       
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request, 'store/checkout.html',context)

def login(request):

    return render(request,'store/login.html')

def signup(request):
    if request.method =='POST':
        user=request.POST.get('username')
        mobile=request.POST.get('mobile')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirmPassword')
        
        if pass1 != pass2:
            messages.error(request,"your password and confirmPassword are not same!")
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            print(newuser.errors)

    return render(request,'store/signup.html')

def logoutpage(request):
    logout(request)
    messages.error(request,'You have logged out!')
    return redirect('/')

def profilepage(request):
   
    return render(request,'store/profile.html')

def about(request):
    user=request.user
    return render(request,'store/about.html',{'user':user})

def contact(request):
    user=request.user
    if request.method=='POST':
        newfeedback=feedbackForm(request.POST)
        if newfeedback.is_valid():
            newfeedback.save()
            print("Your feedback has been submitted!")
            messages.success(request,'Your feedback has been submitted!')
            #Email Sending
            sub=request.POST['subject']
            msg=f'Dear User!\n\nThanks for your feedback\nWe will connect shortly!\n\nThank & Regards!\nNotesApp Team\n+91 6351959948 | help@notesapp.com | www.notesapp.com'
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)


            return redirect('store/home.html')
        else:
            print(newfeedback.errors)
    return render(request,'store/contact.html',{'user':user})



def home(request):
    user=request.user
    context = {'user':user}
    return render(request,'store/home.html',context)

def updateItem(request):
    pass
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
	    orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
	    orderItem.delete()


    return JsonResponse('Item was added', safe=False)


@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        
    else:

        customer, order = guestOrder(request, data) 
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:

            ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
                )
    
    return JsonResponse('Payment submitted..', safe=False)

def productDetail(request,pk):
    product = Product.objects.get(id=pk)


    return render(request,'store/productDetail.html',{'product':product})