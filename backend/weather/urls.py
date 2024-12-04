from django.urls import path
from .views import WeatherApi

urlpatterns = [
     path('<str:name>/', WeatherApi.as_view(), name='weather-api'),
     path('<int:pk>/', WeatherApi.as_view(), name='weather-detail'),
]
