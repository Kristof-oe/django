import requests
from .models import *
from datetime import *

Api="https://api.openweathermap.org/data/3.0/onecall"
Geo="https://api.openweathermap.org/geo/1.0/direct"
Key="bc5b5f0927b2bf8b6ccfdd009c6e9a87"


def getApi(name, limit=1, key=Key):
    details={
        
        "q":name,
        "limit":limit,
        "appid":key
    }
    
    geo_r=requests.get(Geo, params=details)
    geo_r.raise_for_status()
    datas=geo_r.json()
    if not datas:
        
        raise ValueError(f"{name} has not been found")
    
    else: 
        
        lat= datas[0]['lat'],
        lon= datas[0]['lon']

    
    details2={
        
        'lat':lat,
        'lon':lon,
        'exclude':"minutely, alert",
        'appid':key,
        'units':'metric'
    }
    
    weather_r=requests.get(Api, params=details2)
    weather_r.raise_for_status()
    
    return weather_r.json()
    

def getData(name):
    
    datas=getApi(name, limit=1, key=Key)
    
    lat=datas['lat']
    lon=datas['lon']
    
    timezone_offset=datas['timezone_offset']
    
    weatherkey=WeatherKey.objects.create(
        lat=lat,
        lon=lon,
        name=name,
        timezone_offset=timezone_offset
    )
    
    current=datas['current']
    hourly=datas['hourly'][:7]
    daily=datas['daily'][:7]
    current_weather=current['weather'][0]
    
    WeatherDetails.objects.create(
        
        current_key=weatherkey,
        current_dt=datetime.fromtimestamp(current['dt'], tz=timezone.utc) + timedelta(seconds=timezone_offset),
        current_sunrise=datetime.fromtimestamp(current['sunrise'], tz=timezone.utc) + timedelta(seconds=timezone_offset),
        current_sunset=datetime.fromtimestamp(current['sunset'], tz=timezone.utc) + timedelta(seconds=timezone_offset),
        current_temp=current['temp'],
        current_pressure=current['pressure'],
        current_humidity=current['humidity'],
        current_dew_point=current['dew_point'],
        current_clouds=current['clouds'],
        current_visibility=current['visibility'],
        current_wind_speed=current['wind_speed'],
        current_wind_deg=current['wind_deg'],
        current_id=current_weather['id'],
        current_main=current_weather['main'],
        current_description=current_weather['description'],
        current_icon=current_weather['icon']
    
    )
 
    
    for hour_ in hourly:
        
        hourly_weather=hour_['weather'][0]
        
        WeatherDetails2.objects.create(
          
        hourly_key=weatherkey,     
        hourly_dt=datetime.fromtimestamp(hour_['dt'], tz=timezone.utc) + timedelta(seconds=timezone_offset),
        hourly_temp=hour_['temp'],
        hourly_feels_like=hour_['feels_like'],
        hourly_pressure=hour_['pressure'],
        hourly_humidity=hour_['humidity'],
        hourly_dew_point=hour_['dew_point'],
        hourly_clouds=hour_['clouds'],
        hourly_visibility=hour_['visibility'],
        hourly_wind_speed=hour_['wind_speed'],
        hourly_wind_deg=hour_['wind_deg'],
        hourly_wind_gust=hour_['wind_gust'],
        hourly_id=hourly_weather['id'],
        hourly_main=hourly_weather['main'],
        hourly_description=hourly_weather['description'],
        hourly_icon=hourly_weather['icon']
        
    )
            
    for day_ in daily:
        
        daily_weather=day_['weather'][0]
        
        WeatherDetails3.objects.create(
       
        daily_key=weatherkey,
        daily_dt=datetime.fromtimestamp(day_['dt'], tz=timezone.utc) + timedelta(seconds=timezone_offset),
        daily_sunrise=datetime.fromtimestamp(day_['sunrise'], tz=timezone.utc) + timedelta(seconds=timezone_offset),
        daily_sunset=datetime.fromtimestamp(day_['sunset'], tz=timezone.utc) + timedelta(seconds=timezone_offset),
        daily_moonrise=datetime.fromtimestamp(day_['moonrise'], tz=timezone.utc) + timedelta(seconds=timezone_offset),
        daily_moonset=datetime.fromtimestamp(day_['moonset'], tz=timezone.utc) + timedelta(seconds=timezone_offset),
        daily_temp_day=day_['temp']['day'],
        daily_temp_min=day_['temp']['min'],
        daily_temp_max=day_['temp']['max'],
        daily_feels_like_day=day_['feels_like']['day'],
        daily_feels_like_night=day_['feels_like']['night'],
        daily_pressure=day_['pressure'],
        daily_humidity=day_['humidity'],
        daily_dew_point=day_['dew_point'],
        daily_wind_speed=day_['wind_speed'],
        daily_wind_deg=day_['wind_deg'],
        daily_wind_gust=day_['wind_gust'],
        daily_id=daily_weather['id'],
        daily_main=daily_weather['main'],
        daily_description=daily_weather['description'],
        daily_icon=daily_weather['icon'],
        
        )
    

            