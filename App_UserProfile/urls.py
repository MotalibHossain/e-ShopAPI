from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# Import views 
from App_UserProfile.views import Userlogin, UserRegister, Profile, Verify

app_name='App_UserProfile'
urlpatterns = [
    path('user/', Profile, name ='profile' ),
    path('login/', Userlogin, name ='login' ),
    path('registration/', UserRegister, name ='UserRegister' ),
    path('verify/<otp>', Verify, name ='Verify' ),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)