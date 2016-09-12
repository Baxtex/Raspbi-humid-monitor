#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import smtplib
import logging

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13,True)

mail_sent_temp = 0
mail_sent_hum = 0

#Sends email to my address.
def send_email(subject, body):
	smtp_user = ""#Fill in
	smpt_pass = ""#Fill in

	to_add = ""#FIll in
	from_add = smtp_user
	
	header = "To: " + to_add + '\n' + "From: " + from_add + '\n' + subject
	
	s = smtplib.SMTP("smtp.gmail.com",587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	 
	s.login(smtp_user, smpt_pass)
	s.sendmail(from_add, to_add, header + '\n' + body)
	 
	s.quit()
	logging_monitoring("Email sent to admin")

#Prints and logg messages
def logging_monitoring(message):
	current_time = time.strftime("%H:%M:%S")
	current_date = time.strftime("%d/%m/%Y")
	message = "%s %s: %s " % (current_date, current_time, message)
	logging.basicConfig(filename='humid.log',level=logging.INFO)
	logging.info(message + '\n')
	print (message)
	
#Checks temperatures if no mail has been sent within 7 hours
def check_temperature(temperature, mail_sent_temp):
	if(mail_sent_temp == 0):
		if temperature <= 10:
			send_email("Cold","Temperature is now 10 or less degrees celcius, your flowers aren't happy")
		elif(temperature>=32):
			send_email("Hot", "Temperature is now 32 or more degrees celcius, your flowers aren't happy")
		elif(temperature>=42):
			send_email("Hotter than hell", "Temperature is now 45 or more degrees celcius, your flowers are dying!")
		mail_sent_temp = 550
	return mail_sent_temp

#Checks humidity if no mail has been sent within 7 hours
def check_humidity(humidity, mail_sent_hum):
	if mail_sent_hum == 0:
		if humidity < 70:
			send_email("Thirsty","Tomatoes need water")
		mail_sent_hum = 550	
	return mail_sent_hum
	
#Increases timer if email has been sent
def check_timer(mail_sent_temp, mail_sent_hum):
	if(mail_sent_temp != 0):
		mail_sent_temp -= 1
		
	if(mail_sent_hum != 0):
		mail_sent_hum -= 1
		
	return mail_sent_temp, mail_sent_hum
	
logging_monitoring("Starting")
#Monitors temperature and humidity
try:  
	while True:
		humidity, temperature = Adafruit_DHT.read_retry(11, 4)
		data_string = 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
		logging_monitoring(data_string)
		mail_sent_temp = check_temperature(temperature, mail_sent_temp)
		mail_sent_hum = check_humidity(humidity, mail_sent_hum)
		mail_sent_temp, mail_sent_hum = check_timer(mail_sent_temp, mail_sent_hum)
		time.sleep(30) 
		
except KeyboardInterrupt:  	
	GPIO.output(13,False)	
	logging_monitoring("Service exited")
	
#except:  
 #   logging_monitoring("Exception was throwed! Exiting..") 
  
finally:  
    GPIO.cleanup() # this ensures a clean exit  
	