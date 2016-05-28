from speech import Speech

import subprocess
from PIL import Image
from pytesser import *
import sys
import RPi.GPIO as GPIO
from time import sleep

# specific parameter
# the program is executed after the user pressed the start button on the raspberry pi 
touch_power=2    #
touch_gnd=6      #
touch_signal=18  # Getting high voltages when the user pressed the button
key=1
speech = Speech()

#initalizing GPIO pins on the raspberry pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(touch_signal,GPIO.IN)

# loop forever
while True:
  if GPIO.input(touch_signal)== GPIO.HIGH:
    print(key)
    if key==1:
    
      # taking pictures using the webcam connected to the raspberry pi.
      subprocess.Popen(['sudo','fswebcam','-r','1024X768','-S','20','Pic.jpg'],stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
      sleep(2)
      # transform pictures into pure text
      subprocess.Popen(['sudo','tesseract','Pic.jpg','pagetext'],stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
      sleep(2)
      words=open('pagetext.txt','r')
      word=words.read()
      key=0
      # transform text into speech
      speech.text_to_speech(word)
      print("complete")
      
      
      #print(text) some code for testing
      #words.close()
    if GPIO.input(touch_signal) == GPIO.LOW:
      key=1
