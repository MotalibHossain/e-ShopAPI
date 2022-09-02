import email
from email.headerregistry import Address
from email.mime import image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    email = models.EmailField(max_length=30, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    image = models.ImageField(upload_to="UserProfile/", default='UserProfile/profile.png')
    description = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    otp=models.CharField(max_length=25, unique=True)
    is_varified=models.BooleanField(default=False)


    def __str__(self):
        return self.user.username+'---'+ self.email
