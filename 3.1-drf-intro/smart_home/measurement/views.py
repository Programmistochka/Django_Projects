from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Measurement, Sensor
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

class SensorListCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer 




class SensorsView (ListAPIView):
    # Вывод всех датчиков по GET-запросу:
    # GET {{baseUrl}}/sensors/
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementsListView (ListAPIView):
    # Вывод всех измерений по GET-запросу:
    # GET {{baseUrl}}/measurements_list/
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class SensorDetailView (RetrieveUpdateAPIView):
    # Вывод информации по указанному в запросе датчику с детализацией измерений
    # GET {{baseUrl}}/sensors/<id_sensor>/
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer