from apscheduler.schedulers.background import BackgroundScheduler

# Вариант №2 https://www.youtube.com/watch?v=Lzy4G1wZ7NQ

# Рабочий вариант

import requests
from Apiary_online.keys.api_key import API_WEATHER_KEY
import json
import datetime
from .views import writing_values_database
from .auxiliary_functions import get_latest_record_database

def scheduler_api():

    dt_now = datetime.datetime.now()
    print ('\nЗдесь ▼ указано текущее время (время запроса)')
    print(dt_now.strftime("%d.%m.%Y %H:%M:%S"))
    print ('')

    lat = 56.235616
    lon = 36.847135
    lang = 'ru_RU'
    limit = 1
    hours = False
    extra = True

    url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&limit={limit}&hours={hours}"
    # X-Yandex-API-Key: + API_WEATHER_KEY
    header={'X-Yandex-API-Key': API_WEATHER_KEY}

    r = requests.get(url, headers=header)
    data = r.json()

    writing_values_database(data)

# Проверка внесения данных в БД
def checking_database_entry():

    tdelta_hour, dt_now = get_latest_record_database()

    if tdelta_hour > 0:
        print (f'По состоянию на {dt_now} актульность последней записи в БД более чем {tdelta_hour} час.')
        print ('Начинаю формирование и отправку запроса на сервер API Яндекс.Погоды для получения пропущенной записи')

        lat = 56.235616
        lon = 36.847135
        lang = 'ru_RU'
        limit = 1
        hours = False
        extra = True

        url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&limit={limit}&hours={hours}"
        header={'X-Yandex-API-Key': API_WEATHER_KEY}

        r = requests.get(url, headers=header)
        data = r.json()

        writing_values_database(data)

    else:
        print (f'По состоянию на {dt_now} актульность последней записи в БД подтверждена.')

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduler_api, 'cron', minute='04', id='task_time')
    scheduler.add_job(checking_database_entry, 'cron', minute='05', id='checking_database')
    scheduler.start()
    scheduler.shutdown()


# Вариант №1 https://russianblogs.com/article/78281604497/
'''
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

# Включить работу по расписанию
scheduler_plan = BackgroundScheduler () ## Создание экземпляра планировщика
try:
         # Планировщик использует DjangoJobStore ()
    scheduler_plan.add_jobstore(DjangoJobStore(), "default")
         # Установить задачи по времени, метод выбора - интервал, временной интервал - 15 минут
         # Другой способ - выполнить задачу в фиксированное время с понедельника по пятницу, соответствующий код:
    # @register_job(scheduler_plan, 'cron', day_of_week='mon-fri', hour='8', minute='30', second='10',id='task_time')
    # @register_job(scheduler_plan,"interval", minutes=15)
    @register_job(scheduler_plan, 'cron', second='10',id='task_time')
    def my_job():
                 # Напишите здесь задачу, которую хотите выполнить
        print ('10 секунд прошло')
        #pass
    register_events(scheduler_plan)
    scheduler_plan.start()
except Exception as e:
    print(e)
         # Остановить таймер в случае ошибки
    scheduler_plan.shutdown()
'''
