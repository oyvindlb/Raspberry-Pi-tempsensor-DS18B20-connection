
"""
Created on Tue Jun 16 11:17:11 2020

@author: Eier
"""
import requests
import time
import datetime
from datetime import datetime, timedelta
import schedule
import pymysql
import os


class getData:
    def __init__(self):
        self.time_now = time.time()

    #Picks up serial number value
    def sensor(self):
        for i in os.listdir('/sys/bus/w1/devices'):
            if i != 'w1_bus_master1':
                self.ds18b20 = i

    #Reading the temperature and calculates into celsius and fahrenheit
    def read(self):
        location = '/sys/bus/w1/devices/' + self.ds18b20 + '/w1_slave'        
        tfile = open(location)
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        self.celsius = temperature / 1000
        self.farenheit = (self.celsius * 1.8) + 32

    #Prints the values to the screen and SQL 
    def printing(self):
        cursor.execute("INSERT INTO Observation (Date_Time, Celsius, Farenheit) VALUES (%s, %s, %s)", [self.time_now, float(self.celsius), float(self.farenheit)])
        connection.commit()
        print "Current temperature : %0.3f C" % self.celsius
        print "Current temperature : %0.3f F" % self.farenheit

    def kill(self):
        quit()

#Running the class
def starting():
    myClass = getData()
    myClass.sensor()
    myClass.read()
    myClass.printing()
    

if __name__ == '__main__':

    try:
        connection = pymysql.connect("IP-adress", "Username", "Password") #Establish connection to MySQL-server
        cursor = connection.cursor()
        cursor = cursor.execute("USE DATABASENAME") #Select database
        
        #Running the program every 1 minute, when the clock is xx:00
        schedule.every(1).minutes.at(':00').do(starting)
        while True:
            schedule.run_pending()
    except KeyboardInterrupt:
        kill()
                







