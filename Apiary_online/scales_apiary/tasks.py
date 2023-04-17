import requests
from celery import shared_task
from Apiary_online.celery import app

import requests
from Apiary_online.keys.api_key import API_WEATHER_KEY
import json
import datetime
from scales_apiary.views import writing_values_database

@app.task
def get_meteo_api():

    lat = 56.235616
    lon = 36.847135
    limit = 1
    hours = "false"
    
    url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&limit={limit}&hours={hours}"
    header={'X-Yandex-API-Key': API_WEATHER_KEY}
    
    r = requests.get(url, headers=header)
    
    if r.status_code == 200:
        data = r.json()        
        writing_values_database(data)        
        return True
    return False

'''
@app.task()
def write_file(email):
    send(email)
    return True

@app.task
def get_api():
    response = requests.get('https://api.publicapis.org/categories')
    if response.status_code == 200:
        save_categories(response.json())
        return True
    return False

@app.task()
def test_task():
    print('Worked')
    return True
'''