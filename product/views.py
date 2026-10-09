from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache #####

from rest_framework import mixins, generics

from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer

CACHE_KEY_CATEGORIES = 'categories'
CACHE_TTL = 60

class CategoryListCreateView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset #### фильтр по параметрам

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) # получение категорий

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) # создание категорий
    

class CategoryDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)










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
