from django.contrib import admin
from App_store.models import Category, Product, SubCategory

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)