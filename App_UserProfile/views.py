
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout, authenticate

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
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username).first()

        if user is not None:
            profile=UserProfile.objects.filter(user=user).first()
            if profile.is_varified == True:
                user_password_authenticate=authenticate(username=username, password=password)

                if user_password_authenticate is not None:
                    login(request, user)
                    return redirect(reverse_lazy("App_store:home"))
                else:
                    messages.warning(request, "Password is incorrect.Please enter your valid password")
                    return redirect(reverse_lazy("App_UserProfile:login"))
            else:
                messages.error(request, "Your profile isn't verified.Please, Check your mail and verified your account first")
                return render(request, 'Userprofile/login.html')
        else:
            messages.warning(request, "User is not found")
            return redirect(reverse_lazy("App_UserProfile:login"))






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
            messages.success(request, "Successfully registration complete.Please, check your mail and verify your account")
            return redirect(reverse_lazy('App_UserProfile:login'))
        except Exception as e:
            messages.success(request, e)
            return render(request, 'Userprofile/register.html')

            
    return render(request, 'Userprofile/register.html')

def logoutView(request):
    logout(request)
    return redirect(reverse_lazy("App_store:home"))


def Profile(request):
    return render(request, 'Userprofile/profile.html')

def Verify(request, otp):
    profile_verified=UserProfile.objects.filter(otp=otp).first()

    if profile_verified:
        if profile_verified.is_varified == True:
            messages.success(request, "👍 > Your account already varified.Please login.")
            return redirect(reverse_lazy('App_UserProfile:login'))
        else:
            profile_verified.is_varified=True
            profile_verified.save()
            messages.success(request, 'Successfully verified your account. Now you can login')
            return redirect(reverse_lazy('App_UserProfile:login'))

def Send_Mail_Varification(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )

