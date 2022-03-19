from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name="index"),
    path('search',views.search,name="search"),
    path('signin',views.signin,name="signin"),
    path('login',views.logIn,name="login")
    
]
