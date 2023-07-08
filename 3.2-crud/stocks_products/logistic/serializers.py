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
        print(validated_data)
        positions = validated_data.pop('positions')
        # обновление данных склада по его параметрам 
        stock = super().update(instance, validated_data)
        
        # обновление связанных таблиц
        # в данном случае: таблицы StockProduct
        # с помощью списка positions
        for position in positions:
            #StockProduct.objects.update(stock = stock,**position)
            #StockProduct.objects.update(stock = stock, product = position['product'], quantity = position['quantity'], price = position['price'])
            ProductPositionSerializer.update(self, instance = position['product'], validated_data = {'quantity': position['quantity'], 'price': position['price']} )
        return stock



        #     sp=StockProduct.objects.filter(product = position['product']).data
        #     print(sp)
        #     #ProductPositionSerializer.update(self, instance = position['product'], validated_data = {'quantity': position['quantity'], 'price': position['price']} )
        
        # for position in positions:
        #     print ('position: ', position)
        #     # КАК ПРОВЕРИТЬ ЕСТЬ ЛИ ПРОДУКТ НА СКЛАДЕ?
        #     # сравнить со значениями в таблице Product с идентификатором данной позиции
            
        #     prod_in_stock = Product.objects.filter(positions=position)
        #     print('prod_in_stock :', prod_in_stock)
        #     if position in prod_in_stock:
        #     # если данная позиция уже есть на складе
        #     # все поля по данной позиции необходимо обновить
        #         print ('Есть на складе, обновлена')
        #         # StockProduct.objects.update(stock = stock,**position)
        #         pass
        #     else:
        #     # если данной позиции нет на складе
        #     # необходимо ее создать
        #         print ('Нет на складе, добавлена')
        #         # StockProduct.objects.create(stock = stock,**position)
        #         pass 
        
