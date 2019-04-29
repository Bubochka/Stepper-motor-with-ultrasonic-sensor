# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:09:33 2018

@author: Home
"""

import RPi.GPIO as GPIO
import time

def maalultralyd(TRIGGER, ECHO):
    GPIO.output(TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(TRIGGER, GPIO.LOW)

    while GPIO.input(ECHO)==0: #Dette giver en start og slut tid, der bruges til
        pulse_start_time = time.time() #at beregne distancen
    while GPIO.input(ECHO)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time #start tid - slut tid  
    distance = round(pulse_duration * 17150, 2) #halvdelen af ultralyds hastighed er 17150
    print("Distance:",distance,"cm")
    return distance