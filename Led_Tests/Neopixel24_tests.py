import time
import datetime as dt
import board
import neopixel
import adafruit_veml7700
import busio

#setting upn the communication:
i2c=busio.I2C(board.SCL,board.SDA)
veml7700=adafruit_veml7700.VEML7700(i2c)

pixel_pin = board.D18
num_pixels = 12
ORDER = neopixel.GRB

# colors = (R,G,B)
color_dict={"red":(255,0,0), "green":(0,255,0), "blue":(0,0,255)} #, "Orange":(255,165,0), "SpaceBot Blue":(65,182,230), "White":(255,255,255)

brightness_list=[1,0.8,0.6,0.4,0.2]

def make_pixels(bri):
    pixels = neopixel.NeoPixel(
		pixel_pin, num_pixels, brightness=bri, auto_write=False, pixel_order=ORDER
		)
    return pixels

def demo_led():
    measures={"red":[],"green":[],"blue":[]}
    
    for color in color_dict:
        print("color changed")
        
        for bri in brightness_list:
            pixels=make_pixels(bri)
            print("brightness changed")
            
            for pix in range(num_pixels):
                pixels[pix] = color_dict[color]
                
            pixels.show()
            print("comfig displayed")
            time.sleep(3)
            lux=veml7700.lux
            measures[color].append(lux)
            print("measure added:",lux,"for brightness: ",bri,"in ",measures[color])
            print(lux)
            time.sleep(2)
    return measures
            
start_time=dt.datetime.now()
delta=dt.timedelta(seconds=1)
print('Started : ', start_time, 'timedelta= ',delta)

measures_dict=demo_led()
print(measures_dict)

import matplotlib.pyplot as plt

x=[5,10,15,20,25]
plt.plot(x,measures_dict['red'],color='red',label='Red')
plt.plot(x,measures_dict['green'],color='green',label='Green')
plt.plot(x,measures_dict['blue'],color='blue',label='Blue')

plt.legend()
plt.title("Lux values per color with various brightness on SpacebotLED")
plt.xlabel('time(s)')
plt.ylabel('lux')
plt.savefig(f"lux_colors{start_time}.png")

"""
new_color=(250,0,250)

pixels=make_pixels()
for pix in range(num_pixels):
    pixels[pix] = new_color
pixels.show()
"""