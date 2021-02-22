from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List': '/products/',
    'Detail View': '/products/<str:pk>/',
    'Create': '/product-create/',
    'Update': '/product-update/<str:pk>/',
    'Delete': '/product-delete/<str:pk>/'
  }
  return Response(api_urls)

@api_view(['GET'])
def product_list(request):
  products = Product.objects.all()
  serializer = ProductSerializer(products, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk):
  product = Product.objects.get(id=pk)
  serializer = ProductSerializer(product, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def product_create(request):
  serializer = ProductSerializer(data=request.data)
  
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['POST'])
def product_update(request, pk):
  product = Product.objects.get(id=pk)
  serializer = ProductSerializer(instance=product, data=request.data)
  
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['DELETE'])
def product_delete(request, pk):
  product = Product.objects.get(id=pk)
  product.delete()
  return Response('Product Deleted!')
   