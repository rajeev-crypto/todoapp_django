from django.contrib import admin
# from django.urls import path,include
# Register your models here.

from .models import Todolist

admin.site.register(Todolist)