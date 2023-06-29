from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Measurement, Sensor
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

class SensorListCreate(ListCreateAPIView):
    # Вывод всех датчиков по GET-запросу:
    # GET {{baseUrl}}/sensors/
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer 


    def post (self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
   
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