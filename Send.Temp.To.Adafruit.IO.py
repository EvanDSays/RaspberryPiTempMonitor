import os
import glob
import time
from Adafruit_IO import Client, Feed, Data, RequestError

#Read temperature from sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
f = open(device_file, 'r')
lines = f.readlines()
f.close()
while lines[0].strip()[-3:] != 'YES':
    time.sleep(0.2)
    lines = read_temp_raw()
equals_pos = lines[1].find('t=')
if equals_pos != -1:
    temp_string = lines[1][equals_pos+2:]
    temp_c = float(temp_string) / 1000.0
    temp_f = temp_c * 9.0 / 5.0 + 32.0

#Send data to Adafruit.IO

#CHANGE THESE THREE VARIABLES
ADAFRUIT_IO_USERNAME = "YOUR_ADAFRUIT_IO_USERNAME_HERE"
ADAFRUIT_IO_KEY = "YOUR_ADAFRUIT_IO_KEY_HERE"
ADAFRUIT_FEED = "YOUR_ADAFRUIT_FEED_HERE"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#If you want to use Celcius, uncomment the below line and comment out the line with temp_f
#data = Data(value=temp_c)
data = Data(value=temp_f)

#Sends the data to Adafruit.IO
aio.create_data(ADAFRUIT_FEED, data)
