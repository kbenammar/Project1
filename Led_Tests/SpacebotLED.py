import time
import datetime as dt
import random
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


def make_pixels(bri):
    pixels = neopixel.NeoPixel(
		pixel_pin, num_pixels, brightness=bri, auto_write=False, pixel_order=ORDER
		)
    return pixels

bri=1
pixels=make_pixels(bri)
purple=(250,0,250)

def stop_action():
    pixels=make_pixels(0)
    pixels.fill((0,0,0))
    pixels.show()

def solid(color):
    bri=1
    pixels=make_pixels(bri)
    pixels.fill(color)
    pixels.show()

def default_setup():
    bri=.3
    default_color=(65,182,230)
    pixels=make_pixels(bri)
    for pix in range(num_pixels):
        pixels[pix] = default_color
    pixels.show()


def blink_disco(show,hide):
    bri=1
    pixels = make_pixels(bri)
    for i in range(num_pixels):
        pixels[i]=(random.randrange(0,250),random.randrange(0,250),random.randrange(0,250))
    pixels.show()
    time.sleep(show)
    pixels.fill((0,0,0))
    pixels.show()
    time.sleep(hide)


def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos*3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3) 
    return (r,g,b)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range (num_pixels):
            pixel_index=(i*256 // num_pixels)+j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
        
def bingo_action():
    rainbow_cycle(0)
    pixels.fill((0,0,0))
    pixels.show()
    time.sleep(.2)
    rainbow_cycle(0.0001)


def picture_flash(value):
    white=(255,255,255)
    bri_lst=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    show=.1
    hide=.3
    for bri in bri_lst:
        pixels=make_pixels(bri)
        pixels.fill(white)
        pixels.show()
        time.sleep(1)
        measure = veml7700.lux
        print(measure)
        if measure >= value and measure <= value+10:
            print("correct brightness")
            pixels=make_pixels(bri)
            pixels.fill((0,0,0))
            pixels.show()
            time.sleep(hide)
            pixels.fill(white)
            pixels.show()
            time.sleep(show)
            pixels.fill((0,0,0))
            pixels.show()
            print("picture taken")
            break
        
def loading_cycle(color):
    pixels=make_pixels(bri)
    for pix in range(num_pixels):
        pixels[pix]=color
        time.sleep(0.1)
        pixels.show()
    time.sleep(.3)
    
def pulse(color,dark,speed):
    bri_lst=[0,0.05,0.1,0.15,0.20,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1]
    pixels=make_pixels(0)
    pixels.fill((0,0,0))
    pixels.show()
    time.sleep(dark)
    for bri in bri_lst[::-1]:
        pixels=make_pixels(bri)
        pixels.fill(color)
        pixels.show()
        time.sleep(speed)