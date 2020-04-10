# Script to pull temperature from DHT11 sensor using adafruit module
import sys
import Adafruit_DHT
import datetime

#this will only let you pull from DHT11 connected to GPIO 2
sensor = Adafruit_DHT.DHT11
pin = 2

#convert celsius to farenheight because Merica
temperature = temperature * 9/5.0 + 32

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*F  Humidity={1:0.1f}% Time={2}'.format(temperature, humidity, datetime.now))
	with open('templog.txt'),'a') as f:
	print('Temp={0:0.1f}*F  Humidity={1:0.1f}% Time={2}'.format(temperature, humidity, datetime.now))
else:
    print('Failed to get reading. Try again!')
sys.exit()