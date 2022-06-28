#importing libraries
import time
import datetime as dt
import numpy as np
import argparse
import board
import busio
import adafruit_tsl2591

#setting the file name argument:
parser=argparse.ArgumentParser()
parser.add_argument("file_name", type=str, help="enter the name of the file") 

args=parser.parse_args()
print(args)
file = args.file_name

#setting upn the communication:
i2c=board.I2C()
tsl2591=adafruit_tsl2591.TSL2591(i2c)

f=open(file,'w')

start_time=dt.datetime.now()
delta=dt.timedelta(minutes=1)
print('Started : ', start_time, 'timedelta= ',delta)

luxLst=[]
while True:
    # setting time
    now=dt.datetime.now()
    print(now)
    # setting measures
    lux=tsl2591.lux
    luxLst.append(lux)
    
    if len(luxLst)==60:
        #load the data 
        data={'date' : dt.datetime.now().strftime("%d/%m/%y|%H:%M:%S") , 'mean_light' : round(np.mean(luxLst),2),
              'min_light' : round(np.min(luxLst),2), 'max_light' : round(np.max(luxLst),2), 'variance' : round(np.var(luxLst),2)}
        f.write(str(data))
        luxLst.clear()
    time.sleep(1)

