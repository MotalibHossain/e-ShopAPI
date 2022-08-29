from cProfile import Profile
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Userlogin(request):
    return render(request, 'UserProfile/login.html')

def UserRegister(request):
    return render(request, 'UserProfile/register.html')


def Profile(request):
    return HttpResponse("User Profile")

