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

@api_view(['GET', 'PUT'])
def CategoryUpdate(request, pk):
    if request.method == 'GET':
        updatecategory=Category.objects.filter(pk=pk)
        serializer = CategorySerializer(updatecategory,  many=True)
        return Response(serializer.data)

    if request.method == 'PUT':
        update_category = CategorySerializer(data=request.data)
        if update_category.is_valid():
            update_category.save()
            return Response(update_category.data)
        else:
            return Response(update_category.errors)


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

@api_view(['GET', 'PUT'])
def ProductUpdate(request, pk):
    if request.method =='GET':
        update_product=Product.objects.filter(pk=pk)
        serializer = ProductSerializer(update_product,  many=True)
        return Response(serializer.data)

    if request.method == 'PUT':
        update_serializer=ProductSerializer(data=request.data)
        if update_serializer.is_valid():
            return Response(update_serializer.data)
        else:
            return Response(update_serializer.errors)



