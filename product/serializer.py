from rest_framework import serializers
from decimal import Decimal
from .models import Product, Category
from .validator import valid_title

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')
        read_only_fields = ('id',)

# class ProductSer(serializers.Serializer): - метод ручной сериализации данных 
#     id = serializers.IntegerField(read_only = True)
#     title = serializers.CharField(max_length=100, )
#     description = serializers.CharField(required = False, allow_blank=True)

class ProductSerializer(serializers.ModelSerializer): # автоматический метод сериализации 
    final_price = serializers.SerializerMethodField(read_only=True)

    title = serializers.CharField(max_length=100, validators=[valid_title])

    class Meta:
        model = Product
        fields = ('__all__')
        read_only_fields = ('id', 'created_at', 'update_et')

    def get_final_price(self, obj: Product) -> str:
        if obj.discount > 0:
            multipler = Decimal(1) - (Decimal(obj.discount) / Decimal(100))
            return str(round(obj.price * multipler, 2))
        return str(obj.price) # вывод финальной цены

    