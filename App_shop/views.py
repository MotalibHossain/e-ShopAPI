from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class Home(View):
    
    def get(self, request):
        return HttpResponse("shop home")