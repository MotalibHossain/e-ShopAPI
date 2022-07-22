from django.db import models
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse_lazy

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)
    category_img=models.ImageField(upload_to="shop/image/category/")

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    Subcatagory=models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    category_img=models.ImageField(upload_to="shop/image/Subcategory/")

    def __str__(self):
        return self.name


class Product(models.Model):
    catagory=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='Product_catagory')
    sub_category=models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name=models.CharField(max_length=80, null=True)
    slug=models.SlugField(max_length=80, unique=True)
    description=models.TextField()
    Product_img=models.ImageField(upload_to='shop/images/Product/')
    old_price=models.DecimalField(max_digits=7,decimal_places=2)
    new_price=models.DecimalField(max_digits=7, decimal_places=2)
    is_active=models.BooleanField(default=True)
    is_stock=models.BooleanField(default=True)
    published_date=models.DateField(auto_now_add=True)
    update_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name +"------"+ self.slug
    
    class Meta:
        ordering=['-published_date',]

    def get_absolute_url(self):
        return reverse_lazy('App_store:Product_Details', args=[self.slug])
