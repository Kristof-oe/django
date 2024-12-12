from rest_framework import serializers
from .models import *

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model=WeatherKey, WeatherDetails3, WeatherDetails2, WeatherDetails
        fields= '__all__'