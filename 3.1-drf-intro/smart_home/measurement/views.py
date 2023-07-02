from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Measurement, Sensor
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

class SensorListCreate(ListCreateAPIView):
    # Вывод всех датчиков по GET-запросу:
    # GET {{baseUrl}}/sensors/
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer 

    # Добавление нового датчика по POST-запросу:
    # POST {{baseUrl}}/sensors/
    def post (self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
   
class MeasurementsListView (ListCreateAPIView):
    # Вывод всех измерений по GET-запросу:
    # GET {{baseUrl}}/measurements_list/
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    # Добавление нового показатние по POST-запросу:
    # POST {{baseUrl}}/measurements/
    def post (self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

class SensorDetailView (RetrieveUpdateAPIView):
    # Вывод или обновление информации по указанному в запросе датчику с детализацией измерений
    # GET {{baseUrl}}/sensors/<id_sensor>/
    # PATCH {{baseUrl}}/sensors/<id_sensor>/
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    