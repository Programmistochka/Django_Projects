from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete = models.CASCADE, related_name='mesurements')
    temperature = models.DecimalField(max_digits = 3, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add = True) #автозаполнение даты и времени создания записи
    