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

    class Meta:
        ordering = ['beehive_number']

    def __str__(self):
        return (f'id={(self.id)}; улей № {(self.beehive_number)}; матка № {(self.zeichen_konigin)}; '
        f'начало засева {(self.eiablage_seit)}; порода {(self.konigin_rasse)}; линия {(self.konigin_linie)}; '
        f'материнская линия {(self.muttervolk)}; отцовская линия {(self.drohnenvolker)}')

# unique = True ► атрибут указывает, что значение должно быть уникальным.
# null = True ► в ячейке таблицы БД значение поля будет равно null, если не передадётся значение поля в модели.
# blank = True ► поле будет необязательным к заполнению.

class Weight_2(models.Model):
    beehive_number = models.ForeignKey(Bienenkonigin_1, on_delete=models.DO_NOTHING) 
    date_time_weight_fixation = models.DateTimeField('date and time of weighing')
    weight_beehive = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'id={(self.id)}; улей № {(self.beehive_number.beehive_number)}; {(self.date_time_weight_fixation)}; {(self.weight_beehive)}'
        
class Weather_3(models.Model):
    date_time_fixing_values = models.DateTimeField(verbose_name = "Дата/Время")
    air_temperature_sensor = models.SmallIntegerField(null = True, verbose_name = "t(°C)")
    air_temperature_api = models.SmallIntegerField(null = True, verbose_name = "t(API, °C)")
    air_humidity_sensor = models.PositiveSmallIntegerField(null = True, verbose_name = "ф(%)")
    air_humidity_api = models.PositiveSmallIntegerField(null = True, verbose_name = "ф(API, %)")
    atmospheric_pressure_api = models.PositiveSmallIntegerField(null = True, verbose_name = "p(API)")
    wind_power_api = models.DecimalField(null = True, max_digits=4, decimal_places=1, verbose_name = "ветер")
    wind_gust_api = models.DecimalField(null = True, max_digits=4, decimal_places=1, verbose_name = "порывы")
    wind_direction_api = models.CharField(max_length=20, blank = True, verbose_name = "направление ветра")
    wind_direction_ico_url = models.CharField(max_length=100, blank = True)
    weather_description_api = models.CharField(max_length=100, blank = True, verbose_name = "описание")
    weather_description_ico_url = models.CharField(max_length=100, blank = True)
    daytime_api = models.CharField(max_length=1, blank = True, verbose_name = "D/N")

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return "id=" + str(self.id) + "; " + str(self.date_time_fixing_values) + "; " + str(self.air_temperature_sensor) + "; " + str(
        self.air_temperature_api) + "; " + str(self.air_humidity_sensor) + "; " + str(self.air_humidity_api) + "; " + str(
        self.atmospheric_pressure_api) + "; " + str(self.wind_power_api) + "; " +  str(self.wind_direction_api) + "; " + str(
        self.weather_description_api)

# date_time_weight_fixation = models.ForeignKey(Weight_2, on_delete=models.CASCADE)
# ▲ Попробовать в случае активации связей с Weight_2.date_time_weight_fixation