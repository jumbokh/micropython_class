from umqtt.simple import MQTTClient
import machine,dht,utime,time,network
import config

mq_server = 'broker.emqx.io'
mq_id = 'esp00001' 
mq_topic = b'room_status'
mq_user=''
mq_pass=''
SSID = config.SSID        # WiFi名稱
PASSWORD = config.PASSWORD   # WiFi密碼
d11=dht.DHT11(machine.Pin(15))      # GPIO14 as the DHT11 dataline
wifi= network.WLAN(network.STA_IF)
wifi.active(True)

try:
    #wifi.connect(SSID, PASSWORD)
    print('start to connect wifi')
    for i in range(20):
        print('try to connect wifi in {}s'.format(i))
        utime.sleep(1)
        if wifi.isconnected():
            break          
    if wifi.isconnected():
        print('WiFi connection OK!')
        print('Network Config=',wifi.ifconfig())
    else:
        print('WiFi connection Error')      
    mqClient0 = MQTTClient(mq_id, mq_server, user=mq_user, password=mq_pass)
    mqClient0.connect()
    i=0
    while True:
        d11.measure()
        mq_message='T={},H={}'.format(d11.temperature(),d11.humidity())
        mqClient0.publish(mq_topic, mq_message)
        time.sleep(5)
        i=i+1
        print(mq_message,"message publish {}".format(i))
except Exception as e: print(e)