from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import *
from .models import *


def index(request):
    msg = ""
    if request.method == 'POST':
        if request.POST.get('signup') == 'signup':
            newuser = signupForm(request.POST)
            if newuser.is_valid():
                username=newuser.cleaned_data.get('username')
                try:
                    user_register.objects.get(username=username)
                    print("Username Is already exists ")
                    msg="Username Is already exists"
                
                except user_register.DoesNotExist:
                    newuser.save()
                    print("Signup Successfully!")
                    msg = "Signup Successfully!"
            else:
                print(newuser.errors)
                msg = "Error!Something went wrong...Try again!"
        elif request.POST.get('login') == 'login':
            unm = request.POST['username']
            pas = request.POST['password']
            user = user_register.objects.filter(username=unm, password=pas)
            if user:  # TRUE
                msg = "Login Successfull!"
                print("Login Successfull!")
                request.session['user'] = unm
                return redirect('notes')
            else:
                print("Error!Login faild.....")
                msg = "Error!Login faild....."
    return render(request, 'index.html', {'msg': msg})


def contacts(request):
    return render(request, 'contacts.html')


def notes(request):
    user = request.session.get('user')
    if request.method=='POST':
        newnotes=NotesForm(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been submitted!")
        else:
            print(newnotes.errors)
    return render(request, 'notes.html', {'user': user})


def about(request):
    return render(request, 'About.html')

def updateProfile(request):
    return render(request,'updateProfile.html')

def user_logout(request):
    logout(request)
    msg="User Logged Out Successfully"
    return redirect('/')
