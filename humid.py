#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import smtplib

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13,True)

#Sends mail to my address.

def send_email(subject, body):
	smtp_user = "My-email"
	smpt_pass = "My-pass"
	
	to_add = "Receiver mail"
	from_add = smtp_user
	
	header = "To: " + to_add + '\n' + "From: " + from_add + '\n' + subject
	
	s = smtplib.SMTP("smtp.gmail.com",587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	 
	s.login(smtp_user, smpt_pass)
	s.sendmail(from_add, to_add, header + '\n' + body)
	 
	s.quit()

#Prints and logg messages
	
def logging(message):
	current_time = time.strftime("%H:%M:%S")
	current_date = time.strftime("%d/%m/%Y")
	message = "%s %s: %s " % (current_date, current_time, message)
	print (message)
	
logging("Starting")

#Monitors temperature and humidity

try:  
	while True:
		humidity, temperature = Adafruit_DHT.read_retry(11, 4)
		data_string = 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
		logging(data_string)
		
		if temperature <= 10:
			send_email("Cold","Temperature is now 10 or less degrees celcius, your flowers aren't happy")
		elif(temperature>=32):
			send_email("Hot", "Temperature is now 35 or more degrees celcius, your flowers aren't happy")
		elif(temperature>=42):
			send_email("Hotter than hell", "Temperature is now 45 or more degrees celcius, your flowers are dying!")
		#Har ca 50 i luften
		if humidity < 80:
			send_email("Thirsty","Tomatoes need water")
		
		time.sleep(10) #pauses execution for specified time.
		
except KeyboardInterrupt:  	
	GPIO.output(13,False)	
	

	
	