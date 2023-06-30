from django.urls import path
from .views import SensorListCreate, SensorDetailView, MeasurementsListView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorListCreate.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementsListView().as_view())

]
