from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Bienenkonigin_1
from .models import Weight_2
from .models import Weather_3
import requests
from Apiary_online.keys.api_key import API_WEATHER_KEY
import json
import datetime

def main_page(request):

    ''' ▼ Вывод в браузер текстового сообщения ▼
    return HttpResponse("<b>The main page of the site!!!</b>")
        ▼ Вывод в браузер показания датчика температуры ▼
    meteo_data_all = Weather_3.objects.all()
    return HttpResponse("<b>%s</b>" % ('Температура воздуха равна ' + 
        str(meteo_data_all[1]) + ' °C'
    ))
        ▼ Использование шаблона "meteo_data_table" для вывода в браузер таблицы метеоданных
          с одним значением в столбце ▼
    meteo_data_all = Weather_3.objects.all()
    
    context = {
        #'meteo_data_0': str(meteo_data_all[0])
        'meteo_data_1': str(meteo_data_all[1])
    }
    
    return render(
        request,
        'scales_apiary/meteo_data_table.html',
        context
    )    
       ▼ Использование шаблона "meteo_data_table" для вывода в браузер таблицы метеоданных
         с множеством значений в одном столбце ▼
    
    meteo_data_all = Weather_3.objects.all()
    context = {
        #'meteo_data_0': str(meteo_data_all[0])
        'meteo_data_array': meteo_data_all
    }
    return render(
        request,
        'scales_apiary/meteo_data_table.html',
        context
    )
    '''

    '''
    # ▼ Упорядочивание данных по возрастанию id в таблице БД и таблице шаблона
    def restoring_order(min_id, max_id, excluded_id): # , excluded_id
        for i in range(min_id, max_id):
            if i in excluded_id: # in [19, 23]:
                print (f'Элемент с id={i} отсутствует')
                continue
            obj_id = Weather_3.objects.get(id=i)
            print (obj_id)
            # obj_id.save()

    min_id = 1
    max_id = 19
    excluded_id = [19, 23] # [19, 23]

    # restoring_order(min_id, max_id, excluded_id) # , excluded_id
    '''

    # ▼ Использование шаблона "meteo_data_table" для вывода в браузер таблицы метеоданных
    #   с множеством значений в двух столбцах

    meteo_data_all = Weather_3.objects.all()

    a = meteo_data_all[1]

    # print (a.date_time_fixing_values)
    # print (type(a.date_time_fixing_values))

    dt_now = datetime.datetime.now()
    print ('\nЗдесь ▼ указано текущее время')
    print(dt_now.strftime("%d.%m.%Y %H:%M:%S"))
    print ('')

    # print (meteo_data_all[0])
    # ▲ данные команды выводит на печать в cmd при запуске сервера

    row = 24
    # ▲ данная переменная задаёт количество строк в "таблице метеорологических данных"

    context = {
        #'meteo_data_array': meteo_data_all,
        #'meteo_data_0': str(meteo_data_all[0]),
        #'meteo_data_array': meteo_data_all[:row],
        #'meteo_data_array': meteo_data_all[5:row],
        #'meteo_data_array': meteo_data_all.reverse()[:row],
        'meteo_data_array': meteo_data_all[meteo_data_all.count()-row:],
    }

    return render(
        request,
        'scales_apiary/meteo_data_table.html',
        context
    )
    
def weight_page(request):
    
    # r = requests.get()
    # data = r.json()
    #    Weather_3.objects.create(date_time_fixing_values=data.get('time'), )

    weight_beehives_all = Weight_2.objects.all()

    a = weight_beehives_all[1]

    print (a)
    print (type(a))
    print (a.weight_beehive)
    print (type(a.weight_beehive))
    print (a.beehive_number)
    print (type(a.beehive_number))
    print (a.beehive_number.beehive_number)
    print (type(a.beehive_number.beehive_number))
    # ▲ данные команды выводят на печать в cmd при запуске сервера
    
    context = {
        'weight_beehive_array': weight_beehives_all[:7]
    }
    
    return render(
        request,
        'scales_apiary/beehive_weights_table.html',
        context
    )

def test_request(request):

    return render(
        request,
        'scales_apiary/test_request.html',
    )

def test_response(request):

    name = request.GET ['name']
    phone = request.GET ['phone']
    context = {
        'name': name,
        'phone': phone
    }

    return render(
        request,
        'scales_apiary/test_response.html',
        context
    )

def api_weather_request(request):

    return render(
        request,
        'scales_apiary/api_request.html',
    )

def writing_values_database(data):

    obs_time = data["fact"]["obs_time"] # ◄ время замера погодных данных в формате Unixtime
    date_time = datetime.datetime.fromtimestamp(obs_time)

    temperature_api = data["fact"]["temp"]
    humidity_api = data["fact"]["humidity"]
    pressure_api = data["fact"]["pressure_mm"]

    wind_power_api_tenth = data["fact"]["wind_speed"]
    # wind_power_api_whole = round(wind_power_api_tenth, 0)
    wind_gust_api = data["fact"]["wind_gust"]

    wind_direction_api_upp = data["fact"]["wind_dir"]
    wind_direction_api_cap = wind_direction_api_upp.upper()
    wind_direction_ico_url = "img/wind/" + wind_direction_api_cap + ".png"

    weather_description_api_en = data["fact"]["condition"]
    dict_translat_weather_description = {
        "clear": "ясно",
        "partly-cloudy": "малооблачно",
        "cloudy": "облачно с прояснениями",
        "overcast": "пасмурно",
        "drizzle": "морось",
        "light-rain": "небольшой дождь",
        "rain": "дождь",
        "moderate-rain": "умеренно сильный дождь",
        "heavy-rain": "сильный дождь",
        "continuous-heavy-rain": "длительный сильный дождь",
        "showers": "ливень",
        "wet-snow": "дождь со снегом",
        "light-snow": "небольшой снег",
        "snow": "снег",
        "snow-showers": "снегопад",
        "hail": "град",
        "thunderstorm": "гроза",
        "thunderstorm-with-rain": "дождь с грозой",
        "thunderstorm-with-hail": "гроза с градом"
    }
    weather_description_api_ru = dict_translat_weather_description[weather_description_api_en]

    def upcase_first_letter(s):
        return s[0].upper() + s[1:]

    weather_description_api_ru_f_l = upcase_first_letter(weather_description_api_ru)

    weather_description_ico_url = "img/weather_description/32/" + data["fact"]["icon"] + ".png"

    daytime_api = data["fact"]["daytime"]

    p = Weather_3.objects.create(
        date_time_fixing_values = date_time,
        air_temperature_api = temperature_api,
        air_humidity_api = humidity_api,
        atmospheric_pressure_api = pressure_api,
        wind_power_api = wind_power_api_tenth,
        wind_gust_api = wind_gust_api,
        wind_direction_api = wind_direction_api_cap,
        wind_direction_ico_url = wind_direction_ico_url,
        weather_description_api = weather_description_api_ru_f_l,
        weather_description_ico_url = weather_description_ico_url,
        daytime_api = daytime_api
        )

def api_weather_response(request):

    lat = request.GET ['lat_']
    lon = request.GET ['lon_']
    lang = request.GET ['lang_']
    limit = request.GET ['limit_']
    hours = request.GET ['hours_']
    extra = request.GET ['extra_']

    url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&limit={limit}&hours={hours}"
    # X-Yandex-API-Key: + API_WEATHER_KEY
    header={'X-Yandex-API-Key': API_WEATHER_KEY}

    r = requests.get(url, headers=header)
    data = r.json()

    # json_object = json.dumps(data, indent = 4, ensure_ascii=False)
    # ensure_ascii=False => отмена экранирования ascii символов
    # print(json_object)
    # ▲ Преобразование данных в формат json и вывод на печать ▲

    obs_time = data["fact"]["obs_time"] # ◄ время замера погодных данных в формате Unixtime
    date_time = datetime.datetime.fromtimestamp(obs_time)
    # print(date_time)
    # print (type(date_time)) # <class 'datetime.datetime'>

    date_time_format = date_time.strftime('%Y.%m.%d %H:%M')
    # print(date_time_format)
    # print (type(date_time_format)) # <class 'str'>

    locality_name = data["geo_object"]["locality"]["name"] # ◄ название населенного пункта
    province_name = data["geo_object"]["province"]["name"] # ◄ название региона
    country_name = data["geo_object"]["country"]["name"]

    writing_values_database(data)

    # print (wind_power_api_tenth)
    # print (wind_power_api_whole)
    # print (f'Описание погоды: {weather_description_api_ru}')
    # print (f'Иконка погоды: {(data["fact"]["icon"])}')
    # print (f'Дата и время сервера в UTC = {data["now_dt"]}')
    # print (type(data["now_dt"])) # <class 'str'>
    # print (f'Вывод значения ключа "info" => {data["info"]}')
    # print (type(data["info"]))
    # print (f'Вывод значения ключа "info"/"tzinfo" => {data["info"]["tzinfo"]}')
    # print (type(data["info"]["tzinfo"]))
    # print (r, type(r)) # <Response [200]> <class 'requests.models.Response'>
    # print (url)
    # print(data, type(data)) #  <class 'dict'>
    # print (r.now_dt) # Fatal Python error:
    # print (wind_direction_ico_url)
    # print (type(wind_direction_ico_url))
   
    context = {
        'lat_rp': lat,
        'lon_rp': lon,
        'lang_rp': lang,
        'json_pj': r,
        'obs_time_rp': obs_time,
        'date_time_format_rp': date_time_format,
        'locality_name_rp': locality_name,
        'province_name_rp': province_name,
        'country_name_rp': country_name,
    }

    return render(
        request,
        'scales_apiary/api_response.html',
        context
    )

def chart_1(request):

    d = '01.05.2023'

    context = {
        'date': d,
    }

    return render(
        request,
        'scales_apiary/test_chart.html',
        context
    )

# Графики (тестовый режим)
# ▼ ▼ ▼ ▼ ▼
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


row = 24

last_row = Weather_3.objects.order_by("-id")[0:row]

start_chart_timeline = last_row[row-1].date_time_fixing_values
end_chart_timeline = last_row[0].date_time_fixing_values

# print (start_chart_timeline)
# print (end_chart_timeline)

timeline_values = []
temperature_values = []
temperature_min = []
temperature_optim_min = []
temperature_optim_max = []
humidity_values = []

for value in reversed(last_row):
    timeline_values.append(value.date_time_fixing_values.strftime('%Y.%m.%d %H:%M'))
    temperature_values.append(value.air_temperature_api)
    temperature_min.append(10)
    temperature_optim_min.append(16)
    temperature_optim_max.append(25)
    humidity_values.append(value.air_humidity_api)

# print (timeline_values[0])
# print (timeline_values)
# print (temperature_values)

class LineChartJSONView(BaseLineChartView):

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return timeline_values
        # return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Температура API,°C", "MIN,°C", "Optimal MIN,°C", "Optimal MAX,°C"]
        # return ["Температура,°C", "Влажность воздуха,%", "Атмосферное давление, мм рт. ст."]

    def get_data(self):
        """Return 3 datasets to plot."""
        return [temperature_values, temperature_min, temperature_optim_min, temperature_optim_max]

'''
        return [[75, 44, 92, 25, 44, 95, 35],
                [41, 92, 28, 43, 73, 87, 92],
                [87, 21, 94, 36, 90, 40, 65]]
'''

line_chart = TemplateView.as_view(template_name='test_chart.html')
line_chart_json = LineChartJSONView.as_view()

'''
class LineChartJSONViewH(BaseLineChartView):

    def get_labels(self):
        return timeline_values

    def get_providers(self):
        return ["Влажность,%"]

    def get_data(self):
        return [humidity_values]

line_chart = TemplateView.as_view(template_name='test_chart.html')
line_chart_json = LineChartJSONViewH.as_view()
'''

# ▲ ▲ ▲ ▲ ▲

def line_chart_humidity(request):

    a = datetime.datetime.now()
    d = a.strftime('%d.%m.%Y %H:%M')
    print (type(d))

    context = {
        'current_datetime': d,
    }

    return render(
        request,
        'scales_apiary/chart_humidity.html',
        context
    )

