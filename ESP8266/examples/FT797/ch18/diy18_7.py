# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-38頁
"""

from umqtt.simple import MQTTClient
from machine import Pin
import dht
import machine
import network
import time
import ubinascii

rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
rtc.alarm(rtc.ALARM0, 20000)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

if sta_if.isconnected():
	print('WiFi connected!')
else:
	sta_if.connect('WiFi網路ID', 'WiFi密碼')
	print(sta_if.ifconfig())

config = {
	'broker' : 'mqtt.thingspeak.com',
	'user' : 'cubie',
	'key' : 'JZIYJQEQ5MOF8FE6',
	'id' : 'room/' + ubinascii.hexlify(machine.unique_id()).decode(),
	'topic' : b'channels/352801/publish/WMWBJQS44Y5TAH30'
}

client = MQTTClient(client_id=config['id'],
		 server=config['broker'],
	 	 user=config['user'],
		 password=config['key'])

d = dht.DHT11(Pin(2))

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
	print('Publish data to ThingSpeak.')
	
	d.measure()
	data = 'field1={}&field2={}'.format(
		d.temperature(), 
		d.humidity())
	
	client.connect()
	client.publish(config['topic'],data.encode())
	time.sleep(2)
	client.disconnect()

print('Going to sleep...')
machine.deepsleep()