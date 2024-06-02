from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('contacts/',views.contacts),
    path('notes/', views.notes, name='notes'),
    path('about/',views.about),
    path('updateProfile/',views.updateProfile),
    path('user_logout/',views.user_logout)
]