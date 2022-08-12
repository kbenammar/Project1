import time
import datetime as dt
import random
import board
import neopixel

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

# for pix in range(num_pixels):
#         pixels[pix] = purple
#         pixels.show()
#         time.sleep(1)

# pixels.fill((0,0,0))
# pixels.show()
pixels[:3] = purple
pixels.show()