from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Weather_3
from .models import Weight_2

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
          с множеством значений в одном столбце
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

    ''' ▼ Использование шаблона "meteo_data_table" для вывода в браузер таблицы метеоданных
              с множеством значений в двух столбцах'''
    meteo_data_all = Weather_3.objects.all()

    print (meteo_data_all[0])
    # ▲ данная команда выводит на печать в cmd при запуске сервера

    row = 3
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
    
    weight_beehives_all = Weight_2.objects.all()
    
    a = weight_beehives_all[1]

    print (a)
    print (type(a))
    print (a.weight_beehive)
    print (type(a.weight_beehive))
    # ▲ данные команды выводят на печать в cmd при запуске сервера
    
    context = {
        'weight_beehive_array': weight_beehives_all[:3]
    }
    
    return render(
        request,
        'scales_apiary/beehive_weights_table.html',
        context
    )
