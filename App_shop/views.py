from itertools import product
from unicodedata import category
from urllib import request, response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views import View

# API import
from rest_framework.decorators import api_view
from rest_framework.response import Response
from App_shop.serializers import CategorySerializer, ProductSerializer

from App_shop.models import Category, Product

# Create your views here.


@api_view(['GET', 'POST'])
def Home(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category,  many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'POST'])
def productView(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product,  many=True)
    return Response(serializer.data)


@api_view()
def ProductDetailsView(request, pk):
    product_details = Product.objects.filter(pk=pk)
    # product_details=Product.objects.get(pk=pk) //show problem when get product
    serializer = ProductSerializer(product_details,  many=True)
    return Response(serializer.data)
