
from multiprocessing import context
import profile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse

# thirdparti library
import uuid
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# models import
from django.contrib.auth.models import User
from App_UserProfile.models import UserProfile

# Create your views here.
def Userlogin(request):
    return render(request, 'Userprofile/login.html')


def UserRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confPassword = request.POST.get('confPassword')

        # Profile model fields 
        description = ''
        address = ''
        otp = str(uuid.uuid4())

        try:
            # if(username  != None or email != None or phone != None or password != None):
            #     messages.success(request, 'opps 😎! Please, Fillup your all information.That are very inportant information to create your account')
            #     return render(request, 'Userprofile/register.html')

                
            # Check username  already exits or not
            exist_username = User.objects.filter(username=username).first()
            if(exist_username):
                messages.success(request, 'opps 😛! Your User name already Exits!.Chose another one.')
                return render(request, 'Userprofile/register.html')

            # Check email already exits or not
            exist_email = UserProfile.objects.filter(email=email).first()
            if(exist_email):
                messages.success(request, 'opps 😛! Your email already Exits!.')
                return render(request, 'Userprofile/register.html')

            # Check phone number already exits or not
            exist_phone = UserProfile.objects.filter(phone=phone).first()
            if(exist_phone):
                messages.success(request, 'opps 😛! Your phone number already Exits!.')
                return render(request, 'Userprofile/register.html')

            # Password validation 
            if(password!=confPassword):
                messages.success(request, "opps 😛! Your password dosen't match.")
                return render(request, 'Userprofile/register.html')


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
            Send_Mail_Varification(email, otp)
            messages.success(request, "Successfully register")
            return redirect(reverse_lazy('App_UserProfile:login'))
        except Exception as e:
            messages.success(request, e)
            return render(request, 'Userprofile/register.html')

            
    return render(request, 'Userprofile/register.html')


def Profile(request):
    return HttpResponse("User Profile")

def Verify(request, otp):
    profile_verified=UserProfile.objects.filter(otp=otp).first()

    if profile_verified:
        if profile_verified.is_varified == True:
            messages.success(request, "👍 > Your account already varified.Please login.")
            return redirect(reverse_lazy('App_UserProfile:login'))
        else:
            profile_verified.is_varified=True
            profile_verified.save()
            messages.success(request, 'Check your mail and verify your account then login')
            return redirect(reverse_lazy('App_UserProfile:login'))

def Send_Mail_Varification(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )

