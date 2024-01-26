from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def indexView(request):
    return render(request,'index.html')


def signupview(request):
    if request.method =='POST':
        newuser = signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            return redirect('login.html')
        else:
            print(newuser.errors)
    return render(request,'signup.html')


def loginview(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']
        print(unm)
        print(pas)
        user=userSignup.objects.filter(username=unm,password=pas)
    
        if user: #TRUE
            print("Login Successfully!")
            request.session['user']=unm #create session
            return redirect('/')
        else:
            print("Error!Invalid username or password...")
    return render(request,'login.html')




def aboutview(request):
    return render(request,'about.html')

def listingview(request):
    return render(request,'listing.html')

def blogview(request):
    return render(request,'blog.html')