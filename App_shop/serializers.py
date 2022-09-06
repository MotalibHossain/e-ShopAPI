from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from App_shop.models import Category, Product

class CategorySerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField(max_length=10)
    # category_img=Base64ImageField()
    category_img=serializers.ImageField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

class ProductSerializer(serializers.Serializer):
    name=serializers.CharField()
    slug=serializers.SlugField()
    description=serializers.CharField()
    Product_img=serializers.ImageField()
    price=serializers.DecimalField(max_digits=10, decimal_places=None)
    is_active=serializers.BooleanField()
    is_stock=serializers.BooleanField()
    published_date=serializers.DateField()
    update_date=serializers.DateField()