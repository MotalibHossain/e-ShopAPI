from cProfile import Profile
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Profile(request):
    return HttpResponse("User Profile")

