from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Bienenkonigin_1
from .models import Weight_2
from .models import Weather_3
import requests
from Apiary_online.keys.api_key import API_WEATHER_KEY

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
    #   ▼ Использование шаблона "meteo_data_table" для вывода в браузер таблицы метеоданных
    #     с множеством значений в двух столбцах
    meteo_data_all = Weather_3.objects.all()

    print (meteo_data_all[0])
    # ▲ данная команда выводит на печать в cmd при запуске сервера

    row = 5
    # ▲ данная переменная задаёт количество строк в "таблице метеорологических данных"

    context = {
        #'meteo_data_0': str(meteo_data_all[0])
        'meteo_data_array': meteo_data_all[:row]
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

def api_weather_response(request):

    lat = request.GET ['lat_']
    lon = request.GET ['lon_']
    lang = request.GET ['lang_']

    url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"
    # X-Yandex-API-Key: + API_WEATHER_KEY
    header={'X-Yandex-API-Key': API_WEATHER_KEY}

    r = requests.get(url, headers=header)
    data = r.json()

    print (r)
    print (url)
    # print(data, type(data)) <class 'dict'>
    # print (r.now_dt) -> выдал Fatal Python error:

    context = {
        'lat_rp': lat,
        'lon_rp': lon,
        'lang_rp': lang,
        'json_pj': r,
    }

    return render(
        request,
        'scales_apiary/api_response.html',
        context
    )

