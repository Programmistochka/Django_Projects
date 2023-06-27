from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

class SensorSerializer (serializers.Serializer):
    
    class Meta:
        model = Sensor
        fields = ['name', 'description']

class MeasurementSerializer (serializers.Serializer):

    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'created_at']
