from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    """Cериализатор для продукта"""
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    """Cериализатор для позиции продукта на складе"""
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']
    

class StockSerializer(serializers.ModelSerializer):
    """Cериализатор для склада"""
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']


    def create(self, validated_data):
        """Создание склада с позициями по продуктам"""
        # получение связанных данных для других таблиц
        positions = validated_data.pop('positions')
        # создание склада по его параметрам
        stock = super().create(validated_data)
        # заполнение связанных таблиц
        # в данном случае: таблицы StockProduct
        # с помощью списка positions
        for position in positions:
            StockProduct.objects.create(stock = stock,**position) 
            # В явном виде:
            # StockProduct.objects.create(stock = stock, product = position['product'], quantity = position['quantity'], price = position['price'])
        return stock

    def update(self, instance, validated_data):
        """Обновление данных по складу с позициями по продуктам"""
        # получение связанных данных для других таблиц
        positions = validated_data.pop('positions')
        # обновление данных склада по его параметрам 
        stock = super().update(instance, validated_data)

        # обновление связанных таблиц
        # в данном случае: таблицы StockProduct
        # с помощью списка positions
        for position in positions:
            #if position['product'] in StockProduct.objects.get(stock = stock).items():
            StockProduct.objects.update(stock = stock,**position)
            #else:            
            #   StockProduct.objects.update(stock = stock,**position) 
        return stock
