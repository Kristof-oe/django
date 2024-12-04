from django.db import models

class WeatherKey(models.Model):
    
    lat=models.FloatField()
    lon=models.FloatField()
    name=models.CharField(max_length=200, blank=True)
    timezone_offset=models.FloatField()
    
class WeatherDetails(models.Model):
    
    current_key=models.ForeignKey(WeatherKey, on_delete=models.CASCADE, related_name='curentkey')
    current_dt=models.DateTimeField()
    current_sunrise=models.DateTimeField()
    current_sunset=models.DateTimeField()
    current_temp=models.IntegerField()
    current_feels_like=models.FloatField()
    current_pressure=models.IntegerField()
    current_humidity=models.IntegerField()
    current_dew_point=models.FloatField()
    current_clouds=models.IntegerField()
    current_visibility=models.IntegerField()
    current_wind_speed=models.FloatField()
    current_wind_deg=models.IntegerField()
    current_id=models.IntegerField()
    current_main=models.CharField(max_length=30)
    current_description=models.CharField(max_length=30)
    current_icon=models.CharField(max_length=30)
    
class WeatherDetails2(models.Model):
    
    hourly_key=models.ForeignKey(WeatherKey, on_delete=models.CASCADE, related_name='hourlykey')
    hourly_dt=models.DateTimeField()
    hourly_temp=models.IntegerField()
    hourly_feels_like=models.FloatField()
    hourly_pressure=models.IntegerField()
    hourly_humidity=models.IntegerField()
    hourly_dew_point=models.FloatField()
    hourly_clouds=models.IntegerField()
    hourly_visibility=models.IntegerField()
    hourly_wind_speed=models.FloatField()
    hourly_wind_deg=models.IntegerField()
    hourly_wind_gust=models.IntegerField()
    hourly_id=models.IntegerField()
    hourly_main=models.CharField(max_length=30)
    hourly_description=models.CharField(max_length=30)
    hourly_icon=models.CharField(max_length=30)
    
class WeatherDetails3(models.Model):
    
    daily_key=models.ForeignKey(WeatherKey, on_delete=models.CASCADE, related_name='dailykey')
    daily_dt=models.DateTimeField()
    daily_sunrise=models.DateTimeField()
    daily_sunset=models.DateTimeField()
    daily_moonrise=models.DateTimeField()
    daily_moonset=models.DateTimeField()
    daily_temp_day=models.IntegerField()
    daily_temp_min=models.IntegerField()
    daily_temp_max=models.IntegerField()
    daily_feels_like_day=models.FloatField()
    daily_feels_like_night=models.FloatField()
    daily_pressure=models.IntegerField()
    daily_humidity=models.IntegerField()
    daily_dew_point=models.FloatField()
    daily_wind_speed=models.FloatField()
    daily_wind_deg=models.IntegerField()
    daily_wind_gust=models.IntegerField()
    daily_id=models.IntegerField()
    daily_main=models.CharField(max_length=30)
    daily_description=models.CharField(max_length=30)
    daily_icon=models.CharField(max_length=30)

    