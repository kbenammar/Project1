#importing libraries
import datetime as dt
import argparse
# import keyboard
import board
import busio
import adafruit_veml7700

#setting the file name argument:
parser=argparse.ArgumentParser()
parser.add_argument("file_name", type=str, help="enter the name of the file") 

args=parser.parse_args()
print(args)
file = args.file_name

#setting upn the communication:
i2c=busio.I2C(board.SCL,board.SDA)
veml7700=adafruit_veml7700.VEML7700(i2c)

#logging.basicConfig(filename=file, level=logging.DEBUG, format="%(asctime)s | %(message)s")

# key=keyboard.is_pressed('ENTER')
# key2=keyboard.is_pressed('Esc')

#print('Press ENTER to run the program')

var=1

while var!=2:
    f=open(file,'w')
    now=dt.datetime.now()
    lux=veml7700.lux
    f.write(now '| Light level :' lux 'lux\n')
    time.sleep(1)
    print('Press Esc to stop the program')
    
#     if key2:
#         f.close()
#         break