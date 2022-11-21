from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Weather_3

def main_page(request):

    ''' ▼ Вывод в браузер текстового сообщения
    return HttpResponse("<b>The main page of the site!!!</b>")
    '''
    
    ''' ▼ Вывод в браузер показания датчика температуры
    meteo_data_all = Weather_3.objects.all()
    return HttpResponse("<b>%s</b>" % ('Температура воздуха равна ' + 
        str(meteo_data_all[1]) + ' °C'
    ))
    '''
    
    ''' ▼ Использование шаблона "meteo_data_table" для вывода в браузер таблицы метеоданных
          с одним значением в столбце
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
    '''
    
    ''' ▼ Использование шаблона "meteo_data_table" для вывода в браузер таблицы метеоданных
          с множеством значений в столбце '''
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