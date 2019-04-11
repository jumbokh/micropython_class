# -*- coding: utf-8 -*-

"""
   程式說明請參閱18-22頁
"""

import machine
import ubinascii
import time
import dht
from machine import Pin
from umqtt.simple import MQTTClient

config = {
    'broker':'mqtt.thingspeak.com'
    'user':'cubie',
    'key':'你的MQTT API Key',
    'id' : 'room/' + ubinascii.hexlify(machine.unique_id()).decode(),
    'topic' : b'channels/頻道ID/publish/你的寫入API KEY'
}

client = MQTTClient(client_id=config['id'],
                    server=config['broker'],
                    user=config['user'],
                    password=config['key'])

d = dht.DHT11(Pin(2))
d.measure()

data = 'field1={}&field2={}'.format(
        d.temperature(),
        d.humidity())

client.connect()
client.publish(config['topic'], data.encode())
time.sleep(2)
client.disconnect()