from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

# Спец. класс для управления данными по датчикам с помощью HTTP-запросов
class SensorsView (ListAPIView):
    # Вывод всех датчиков по GET-запросу:
    # GET {{baseUrl}}/sensors/
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    # Создание нового датчика по POST-запросу:
    # POST {{baseUrl}}/sensors/
    # Указываются название и описание датчика
    def post (self, request):
        return Response({'status': 'ok'})

    # Изменение датчика
    # Указываются название и описание
    def patch (self, request):
        return Response({'status': 'ok'})

class SensorView (RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer