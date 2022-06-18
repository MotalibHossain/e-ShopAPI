from distutils.command.upload import upload
from unicodedata import category, name
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)
    category_img=models.ImageField(upload_to="shop/image/category/")