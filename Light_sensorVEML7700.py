#importing libraries
import time
import datetime as dt
import argparse
import numpy as np
import board
import busio
import adafruit_veml7700

#setting the file name argument:
parser=argparse.ArgumentParser()
parser.add_argument("--file_name", default="luxmeasuresVEML7700" , type=str, required=False, help="enter the name of the file") 

args=parser.parse_args()
print(args)
file = args.file_name

#setting upn the communication:
i2c=busio.I2C(board.SCL,board.SDA)
veml7700=adafruit_veml7700.VEML7700(i2c)


f=open(file,'w')

start_time=dt.datetime.now()
delta=dt.timedelta(minutes=1)
print('Started : ', start_time, 'timedelta= ',delta)

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
        data={'date' : dt.datetime.now().strftime("%d/%m/%y | %H:%M:%S") , 'mean_lux' : round(np.mean(luxLst),2),
              'min_lux' : round(np.min(luxLst),2), 'max_lux' : round(np.max(luxLst),2), 'variance_lux' : round(np.var(luxLst),2), 'mean_light' : round(np.mean(lightLst),2),
              'min_light' : round(np.min(lightLst),2), 'max_light' : round(np.max(lightLst),2), 'variance_light' : round(np.var(lightLst),2)}
        f.write(str(data)+"\n")
        luxLst.clear()
    time.sleep(1)
