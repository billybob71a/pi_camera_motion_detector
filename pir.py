import RPi.GPIO as GPIO
import time
import datetime
from camera import TakePhoto
from time import sleep
import sys


SENSOR_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
action = TakePhoto(1,'/var/www/html', 'image')

def my_callback(channel):
    now = datetime.datetime.now()
    time_now = (now.year, now.month, now.day, now.hour, now.minute, now.second)
    with open("movement.txt", "a") as myfile:
        myfile.write('There was movement {}\n'.format(time_now))
    action.snapshot()

try:
    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=my_callback)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print("finish")
GPIO.cleanup()
