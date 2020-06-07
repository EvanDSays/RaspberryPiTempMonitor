# Raspberry Pi Temperature Monitor
This documents my steps to turn my old Raspberry Pi (Model B) into a temperature monitor

# Supplies
1. A Raspberry Pi 
2. A temperature sensor (I used a DS18B20) [example](https://www.amazon.com/ARCELI-DS18B20-Temperature-Electronic-Building/dp/B07DN3R1YW/)
3. Three female-to-female jumper wires [example](https://www.amazon.com/GenBasic-Piece-Female-Jumper-Wires/dp/B01L5ULRUA)

# Step 1: Buy a sensor
I bought the cheapest temperature sensor module I could find that already had the resistor built in.  I ended up getting an Arceli DS18B20 Module on Amazon for $4.99 plus tax.  There are other options, like the SunFounder DS18B20 Temperature Sensor Module, but that was $7.99 so I opted for the cheaper option.

# Step 2: Hook up the sensor
The DS18B20 has three pins. Using female-to-female jumper wires, I plugged:
1. The positve pin on the DS18B20 to the 5 Volt GPIO pin on my Raspberry Pi
2. The negative pin on the DS18B20 to a ground GPIO pin on my Raspberry Pi
3. The out/data pin to GPIO4 on my Raspberry Pi

# Step 3: Configure your pi to read from the sensor
Follow the steps under the **ENABLE THE ONE-WIRE INTERFACE** section [within this Circuit Basics write-up](https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/)

# Step 4: Configure your account at Adafruit.IO
Setup an account at [Adafruit.IO](http://io.adafruit.com) which will be used to store your temperature readings.  Once you have an account, create a feed for the temperature readings.  Take note of the following items:
1. Your Adafruit.IO username
2. Your Adafruit.IO key
3. Your feed's name

# Step 5: Configure the Python code on your Raspberry Pi
1. Install the Adafruit IO python library on your Raspberry Pi by running "pip3 install adafruit-io"
2. Place the [Send.Temp.To.Adafruit.IO.py](https://github.com/EvanDSays/RaspberryPiTempMonitor/blob/master/Send.Temp.To.Adafruit.IO.py) script from this repo on your Raspberry Pi.  You will need to change the Adafruit variables found near the bottom of the script based on the information from step 4 above.
3. Configure the script the run on a schedule by running `crontab -e` on your Raspberri Pi.  Scroll down to the bottom of the file and add an entry like the following: `* * * * * python3 /home/pi/Send.Temp.To.Adafruit.IO.py`. Be sure to change the path to wherever you placed the file.

# Step 6: (Optional) Configure Adafruit.IO integrations
I am using IFTTT to send me an email when the temperature goes above a set threshold.  The Adafruit.IO API allows many other integrations, so feel free to pick the best for your specific use case.
