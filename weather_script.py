#!/usr/bin/python
from sense_hat import SenseHat
import time
import sys

sense = SenseHat()
sense.clear()

try:
    while True:
        temp = sense.get_temperature()
        temp = round(temp, 1)
        print("Temperature C",temp)
        
        humidity = sense.get_humidity()
        humidity = round(humidity, 1)
        print("Humidity:",humidity)
        
        pressure = sense.get_pressure()
        pressure = round(pressure,  1)
        print("Pressure:",pressure)
        
        
        sense.show_message( "Temperature C: " + str(temp) + " Humidity: " + str(humidity) + " Pressure: " + str(pressure) + ":)", scroll_speed=(.08), text_colour=[200,200,200], back_colour=[000,100,130])

        time.sleep(5)
except KeyboardInterrupt:
    pass

sense.clear()