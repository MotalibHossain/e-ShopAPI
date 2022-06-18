
from django.contrib import admin
from django.urls import path

# import views 
from App_shop.views import Home

urlpatterns = [
    path("", Home.as_view(), name="home"),
]
