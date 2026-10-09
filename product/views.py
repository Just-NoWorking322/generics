from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache #####

from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer

CACHE_KEY_CATEGORIES = 'categories'



















# class ProductView(APIView):
#     def get(self, request, *args, **kwargs):
#         products = Product.objects.all().select_related('category')
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, *args, **kwargs):
#         serializer = ProductSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response({
#                 "messs": "Товар успешно создан",
#                 "product": serializer.data ###
#             },
#             status=status.HTTP_201_CREATED
#             )
#         return Response({
#                 "messs": "Ошибка валидации данных", 
#                 "details": serializer.errors ###
#             },
#             status=status.HTTP_400_BAD_REQUEST
#             )
