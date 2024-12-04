from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .services import getData
from .models import *

class WeatherApi(APIView):
    
    def get(self, request, name):
        
        getData(name)
        
        WeatherKey.objects.filter(name=name).delete
        
        key=WeatherKey.objects.get(name=name)
        
        weather1=WeatherDetails.objects.filter(current_key=key).latest('current_dt')
        
        weather2=WeatherDetails2.objects.filter(hourly_key=key)
        
        weather3=WeatherDetails3.objects.filter(daily_key=key)
        
        return Response({
            
            "key": key.name
        })
        
        
        
        



