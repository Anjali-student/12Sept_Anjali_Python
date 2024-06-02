from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.


def index(request):
    if request.method == 'POST':  # true
        newdata = student_Form(request.POST)
        if newdata.is_valid():  # TRUE
            newdata.save()
            print("Your data has been saved!")
        else:
            print(newdata.errors)

    return render(request, "index.html")


def register(request):
    return render(request, "register.html")


def showdata(request):
    return render(request, "showdata.html")
