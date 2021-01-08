# Raspberry-Pi-tempsensor-DS18B20-connection
Program that connects tempsensor (DS18B20) to a raspberry pi, using Python. The program requests new temperature update every single minute and write the results to a database (which must be created in SQL). The database contain a table with three columns for "Date_time", "Celsius" and "Farenheit". 

The Program must be runned directly from the Raspberry Pi. The tempsensor must also be correctly installed and connected to the Raspberry Pi, before running this program is possible.
