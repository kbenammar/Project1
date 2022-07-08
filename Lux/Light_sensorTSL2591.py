#importing libraries
import time
import datetime as dt
import numpy as np
import board
import adafruit_tsl2591
import sqlalchemy as db
from sqlalchemy import create_engine
from data import TSL as TSL

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

#setting up the communication with sensor:
i2c=board.I2C()
tsl2591=adafruit_tsl2591.TSL2591(i2c)

start_time=dt.datetime.now()
delta=dt.timedelta(minutes=1)
print('Started : ', start_time, 'timedelta= ', delta, 'until : ', start_time+delta)


luxLst=[]
visibleLst=[]
while True:
    # setting time
    now=dt.datetime.now()
    print(now)
    # setting measures
    lux=tsl2591.lux
    luxLst.append(lux)
    visible=tsl2591.visible
    visibleLst.append(visible)
    
    if len(luxLst)==60:
        #load the data 
        data = TSL(date = dt.datetime.now().strftime("%y/%m/%d %H:%M:%S") , # drop seconds??
                   mean_lux = round(np.mean(luxLst),2),
                   min_lux = round(np.min(luxLst),2),
                   max_lux = round(np.max(luxLst),2),
                   variance_lux = round(np.var(luxLst),2), 
                   mean_visible = round(np.mean(visibleLst),2),
                   min_visible = round(np.min(visibleLst),2), 
                   max_visible = round(np.max(visibleLst),2), 
                   variance_visible = round(np.var(visibleLst),2)
                   )
        session.add(data)
        session.commit()
        luxLst.clear()
        visibleLst.clear()
    time.sleep(1)

