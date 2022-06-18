from distutils.command.upload import upload
from unicodedata import category, name
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)
    category_img=models.ImageField(upload_to="shop/image/category/")


class Product(models.Model):
    catagory=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='Product_catagory')
    name=models.CharField(max_length=80)
    slug=models.SlugField(max_length=80, unique=True)
    description=models.TextField()
    Product_img=models.ImageField(upload_to='shop/images/Product/')
    price=models.DecimalField(max_digits=7, decimal_places=2)
    is_active=models.BooleanField(default=True)
    is_stock=models.BooleanField(default=True)
    published_date=models.DateField(auto_now_add=True)
    update_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name +"-"+ self.slug
    
    class Meta:
        ordering=['-published_date',]