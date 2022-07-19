# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 15:22:16 2022

@author: kenzi
"""

"""api_key='7c288c678bb0a22647b4f2467e4ab0bd'"""

import time
import datetime as dt

from api_keys import api_key
import requests
import json

import sqlalchemy
from sqlalchemy import create_engine
from base_models import WEATHER,Base
from sqlalchemy import Column, Integer, DateTime, String, Float

engine = create_engine('sqlite:///weather.sqlite')
conn = engine.connect()
Base.metadata.create_all(conn)

from sqlalchemy.orm import Session
session = Session(bind=engine)

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
    weather_info = WEATHER(description = results["weather"][0]["description"],
                         temperature_celcius = results["main"]["temp"],
                         temp_feeling_celcius = results["main"]["feels_like"],
                         humidity_percent = results["main"]["humidity"],
                         pressure_hPa = results["main"]["pressure"],
                         visibility_meters = results["visibility"],
                         cloudiness_percent = results["clouds"]["all"])
 
    time.sleep(1)
    return weather_info

if __name__ = '__main__':
    session.add(get_weather())
    session.commit()
    