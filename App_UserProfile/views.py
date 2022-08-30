
from multiprocessing import context
import profile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse

# thirdparti library 
import uuid
from django.contrib import messages

# models import 
from django.contrib.auth.models import User
from App_UserProfile.models import UserProfile

# Create your views here.
def Userlogin(request):
    return render(request, 'Userprofile/login.html')

def UserRegister(request):
    if request.method == 'POST':
        print("user registration *******************")
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        confPassword=request.POST.get('confPassword')

        description=''
        address=''
        otp=str(uuid.uuid4())

        # try:
        # Check username  already exits or not 
        exist_username=User.objects.filter(username=username).first()
        if(exist_username):
            # messages.success(request, 'opps 😛! Your User name already Exits!.Chose another one.')
            # return redirect(reverse_lazy('App_UserProfile:UserRegister'))
            context={
                 "message":"opps 😛! Your User name already Exits!.Chose another one."
            } 
            return render(request, 'Userprofile/register.html',context)

        # Check email already exits or not 
        exist_email=UserProfile.objects.filter(email=email).first()
        if(exist_email):
            # messages.success(request, 'opps 😛! Your email already Exits!.')
            # return redirect(reverse_lazy('App_UserProfile:UserRegister'))
            context={
                 "message":"opps 😛! Your email already Exits!."
            } 
            return render(request, 'Userprofile/register.html',context)

        # Check phone number already exits or not 
        exist_phone=UserProfile.objects.filter(phone=phone).first()
        if(exist_phone):
            messages.success(request, 'opps 😛! Your phone number already Exits!.')
            return redirect(reverse_lazy('App_UserProfile:UserRegister'))

        # Password validation 
        if(password!=confPassword):
            print("opps 😛! Your password dosen't match.")
            # messages.success(request, "opps 😛! Your password dosen't match.")
            # return redirect(reverse_lazy('App_UserProfile:UserRegister'))
            context1 = {"message": "Password mismatch"}
            return render(request, 'Userprofile/register.html', context1)


        user=User.objects.create(username=username, password=password)
        user.set_password(password)
        user.save()

        profile=UserProfile.objects.create(
            user=user, 
            email=email, 
            phone=phone, 
            description=description, 
            address=address, 
            otp=otp 
            )
        profile.save()
        context={
            "message":"Successfully registration Complete 😎!"
        }
        # return render(request, 'Userprofile/login.html', context)
        return redirect(reverse_lazy('App_UserProfile:login'))
        # except Exception as e:
        #     print(e)
    # else:
    #     context={
    #             "message":"ops not complete 😎!"
    #         }     
    #     return render(request, 'Userprofile/register.html', context)

    return render(request, 'Userprofile/register.html')


def Profile(request):
    return HttpResponse("User Profile")

