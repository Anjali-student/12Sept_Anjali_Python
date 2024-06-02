from django.contrib import admin
from .models import *


class studata(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id','name','dob']

admin.site.register(studinfo,studata)
# Register your models here.


# Register your models here.
