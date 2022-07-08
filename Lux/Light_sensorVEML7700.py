#importing libraries
import time
import datetime as dt
import argparse
import numpy as np
import board
import busio
import adafruit_veml7700
import sqlalchemy as db
from sqlalchemy import create_engine
from data import VEML as VEML

# importing  mapping tool
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Import modules to declare columns and column data types
from sqlalchemy import Column, Integer, DateTime, String, Float

# setting connection to sql database:
engine = create_engine('sqlite:///lux_measures.sqlite') # physical place/path to DataBase
conn = engine.connect() # setting connection bridge to DataBase
Base.metadata.create_all(conn) # creating one connection to DataBase

from sqlalchemy.orm import Session
session = Session(bind=engine) # Running a session (virtual temporary playground to modify database  and test)

#setting upn the communication:
i2c=busio.I2C(board.SCL,board.SDA)
veml7700=adafruit_veml7700.VEML7700(i2c)


start_time=dt.datetime.now()
delta=dt.timedelta(minutes=1)
print('Started : ', start_time, 'timedelta= ',delta, 'until : ', start_time+delta)


luxLst=[]
lightLst=[]
while True:
    # setting time
    now=dt.datetime.now()
    print(now)
    # setting measures
    lux=veml7700.lux
    luxLst.append(lux)
    light=veml7700.light
    lightLst.append(light)
    
    if len(luxLst)==60:
        #load the data 
        data=VEML (date = dt.datetime.now().strftime("%d/%m/%y | %H:%M:%S") ,
                   mean_lux = round(np.mean(luxLst),2),
              min_lux = round(np.min(luxLst),2),
              max_lux = round(np.max(luxLst),2),
              variance_lux = round(np.var(luxLst),2),
              mean_light = round(np.mean(lightLst),2),
              min_light = round(np.min(lightLst),2),
              max_light = round(np.max(lightLst),2),
              variance_light = round(np.var(lightLst),2)
              )
        session.add(data)
        session.commit()
        luxLst.clear()
        lightLst.clear()
    time.sleep(1)
