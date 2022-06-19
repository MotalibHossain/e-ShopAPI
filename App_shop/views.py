from itertools import product
from unicodedata import category
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# API import 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from App_shop.serializers import CategorySerializer, ProductSerializer

from App_shop.models import Category, Product

# Create your views here.
@api_view()
def Home(request):
    category=Category.objects.all()
    serializer=CategorySerializer(category,  many=True)
    return Response(serializer.data)


@api_view()
def productView(request):
    product=Product.objects.all()
    serializer=ProductSerializer(product,  many=True)
    return Response(serializer.data)