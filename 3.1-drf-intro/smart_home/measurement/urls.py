from django.urls import path
from .views import SensorsView, SensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view())
]
