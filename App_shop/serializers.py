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

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category_img = validated_data.get('category_img', instance.category_img)
        instance.save()
        return instance

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

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_stock = validated_data.get('is_stock', instance.is_stock)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.update_date = validated_data.get('update_date', instance.update_date)
        instance.save()
        return instance