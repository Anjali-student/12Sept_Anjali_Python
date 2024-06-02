from django.contrib import admin

# Register your models here.
from .models import *


class studata(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name', 'dob','email','address']


admin.site.register(Student, studata)
