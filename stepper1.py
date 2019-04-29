# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:18:32 2018

@author: Home
"""

import RPi.GPIO as GPIO
import time
import ultraBib
import channel


ControlPin = [16,21,19,20]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.output(13,1)
GPIO.output(12,1)
seq = [[1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1],
       [1,0,0,1]]

TRIGGER = 5 #sætter pins for trigger og echo
ECHO = 6
GPIO.setup(TRIGGER, GPIO.OUT) #Definer input og output
GPIO.setup(ECHO, GPIO.IN)

distanceList = []
stepNummer = 0

while True:
    for times in range(4):
        if times < 2:
            for step in seq:
                for pin in range(4):
                    GPIO.output(ControlPin[pin], step[pin])
                print(step)
                stepNummer += 1
                distance = ultraBib.maalultralyd(TRIGGER, ECHO)                 
                distanceList.append({"delta_t" : 0.5,
                                 "field1": distance,
                                 "field2": stepNummer})
        
                time.sleep(0.5)
        else:
            for step in seq:
                for pin in range(4):
                    GPIO.output(ControlPin[pin], step[-pin-1])
                print(step)
                stepNummer -=1
                distance = ultraBib.maalultralyd(TRIGGER, ECHO)                 
                distanceList.append({"delta_t" : 1,
                                 "field1": distance,
                                 "field2": stepNummer})
        
                time.sleep(0.5)
            
        print(distanceList)
            
    channel.send_data(distanceList)
    distanceList = []
    stepNummer = 0
       
GPIO.cleanup()
  
    





