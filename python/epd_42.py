#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd4in2bc
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
logging.info("epd4in2 Demo")

epd = epd4in2bc.EPD()
logging.info("init")
epd.init()

def show_image(filename):
  logging.info("3.read bmp file")
  Himage = Image.open(os.path.join(picdir, filename))
  HRYimage = Image.open(os.path.join(picdir, filename))
  epd.display(epd.getbuffer(Himage),epd.getbuffer(HRYimage))

def display_clear():
  
  logging.info("Clear")
  epd.Clear()
  
# show_image('5.bmp')
# time.sleep(2)
# display_clear()