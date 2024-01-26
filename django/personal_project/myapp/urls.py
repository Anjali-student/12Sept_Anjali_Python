from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [

    path('',views.indexView),
    path('loginview/',views.loginview),
    path('signupview/',views.signupview),
    path('aboutview/',views.aboutview),
    path('listingview/',views.listingview),
    path('blogview/',views.blogview),
]
