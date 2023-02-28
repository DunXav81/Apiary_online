from django.db import models

# Create your models here.


class Bienenkonigin_1(models.Model):
    beehive_number = models.PositiveSmallIntegerField(default=1)
    zeichen_konigin = models.PositiveSmallIntegerField(default=1)
    eiablage_seit = models.DateField('egg laying start date')
    konigin_rasse = models.CharField(max_length=20)
    konigin_linie = models.CharField(max_length=20)
    muttervolk = models.CharField(max_length=20)
    drohnenvolker = models.CharField(max_length=20)


class Weight_2(models.Model):
    beehive_number = models.ForeignKey(Bienenkonigin_1, on_delete=models.DO_NOTHING)
    date_time_weight_fixation = models.DateTimeField('date and time of weighing')
    weight_beehive = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{(self.id)}; {(self.beehive_number)}; {(self.date_time_weight_fixation)}; {(self.weight_beehive)}'
        
class Weather_3(models.Model):
    date_time_fixing_values = models.DateTimeField('date and time of fixing weather values')
    air_temperature_sensor = models.SmallIntegerField(default=0)
    air_temperature_api = models.SmallIntegerField(default=0)
    air_humidity_sensor = models.PositiveSmallIntegerField(default=0)
    air_humidity_api = models.PositiveSmallIntegerField(default=0)
    atmospheric_pressure_api = models.PositiveSmallIntegerField(default=0)
    wind_power_api = models.PositiveSmallIntegerField(default=0)
    wind_direction_api = models.CharField(max_length=20)
    weather_description_api = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id) + "; " + str(self.date_time_fixing_values) + "; " + str(self.air_temperature_sensor) + "; " + str(
        self.air_temperature_api) + "; " + str(self.air_humidity_sensor) + "; " + str(self.air_humidity_api) + "; " + str(
        self.atmospheric_pressure_api) + "; " + str(self.wind_power_api) + "; " +  str(self.wind_direction_api) + "; " + str(
        self.weather_description_api)

# date_time_weight_fixation = models.ForeignKey(Weight_2, on_delete=models.CASCADE)
# ▲ Попробовать в случае активации связей с Weight_2.date_time_weight_fixation