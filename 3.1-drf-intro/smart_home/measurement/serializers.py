import os
from rest_framework import serializers
from .models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы

class SensorSerializer (serializers.ModelSerializer):
    """Сериализатор для ввода или отображения датчиков"""
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    """Сериализатор для ввода или отображения показаний"""
    class Meta:
        model = Measurement
        # При использовании fields тип для поля sensor_id 
        # будте выбран автоматически: SlugRelatedField (для связи 1-m)
        fields = ['sensor_id', 'temperature', 'created_at']
        
class MeasurementsSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения детальной информации показаний"""
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']

class SensorDetailSerializer(serializers.ModelSerializer):
    """Cериализатор с подробной информацией по датчику"""
    measurements = MeasurementsSerializer(read_only=True, many=True)
    
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
