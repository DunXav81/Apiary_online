import datetime
from .models import Weather_3

# Получение интервала (в часах) между текущим значением времени и 
# последним значением из БД для поля date_time_fixing_values модели Weather_3

def get_latest_record_database():
    
    dt_now = datetime.datetime.now()
    latest_record = Weather_3.objects.latest("id")
    last_time_value = latest_record.date_time_fixing_values
    tdelta = dt_now - last_time_value
    tdelta_sec = tdelta.total_seconds()
    tdelta_hour_tuple = divmod (tdelta_sec, 3600)
    tdelta_hour = tdelta_hour_tuple[0]
    # print (tdelta_hour[0])
    # print (type(tdelta_hour[0]))
    
    return tdelta_hour, dt_now