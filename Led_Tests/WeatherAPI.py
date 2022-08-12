api_key='7c288c678bb0a22647b4f2467e4ab0bd'

import time
import datetime as dt

import requests
import json

import sqlalchemy
from sqlalchemy import create_engine


from sqlalchemy.orm import Session


start_time=dt.datetime.now()
delta=dt.timedelta(minutes=1)
print('Started : ', start_time, 'timedelta= ', delta, 'until : ', start_time+delta)

"MERCH MART 41.8881° N, 87.6353° W"

def get_weather():
    merchandise_mart_latlon=(41.8881, 87.6353)
    lat = merchandise_mart_latlon[0]
    lon = merchandise_mart_latlon[1]
    unit = "metric"
    language="en"
    request_url= f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={unit}&lang={language}&appid={api_key}"
    results = requests.get(request_url).json()
    return results

if __name__ == '__main__':
    get_weather()