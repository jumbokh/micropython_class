# xtools.py
from machine import Pin
import urandom, math
import time, network, urequests
import ubinascii
import machine
import config

def get_id():
    return ubinascii.hexlify(machine.unique_id())

def get_num(x):
    return float("".join(ele for ele in x if ele.isdigit() or ele =="."))

def random_in_range(low=0, high=1000):
    r1 = urandom.getrandbits(32)
    r2 = r1 % (high-low) + low
    return math.floor(r2)

def map_range(x, in_min, in_max, out_min, out_max):
   return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)
   
def connect_wifi_led(ssid=config.SSID, passwd=config.PASSWORD, timeout=15):
    wifi_led=Pin(2, Pin.OUT, value=1)
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    start_time=time.time() # 記錄時間判斷是否超時
    if not sta.isconnected():
        print("Connecting to network...")
        sta.connect(ssid, passwd)
        while not sta.isconnected():
            wifi_led.value(0)
            time.sleep_ms(300)
            wifi_led.value(1)
            time.sleep_ms(300)
            # 判斷是否超過timeout秒數
            if time.time()-start_time > timeout:
                print("Wifi connecting timeout!")
                break
    if sta.isconnected():
        wifi_led.value(0)
        print("network config:", sta.ifconfig())
        return sta.ifconfig()[0] 

def show_error(final_state=0):
    led = Pin(2, Pin.OUT)   # Built-in D4
    for i in range(3):
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
    led.value(final_state)    

def webhook_post(url, value):
    print("invoking webhook")
    from xrequests import post
    r = post(url, data=value)
    if r is not None and r.status_code == 200:
        print("Webhook invoked")
    else:
        print("Webhook failed")
        show_error()

def webhook_get(url):
    print("invoking webhook")
    r = urequests.get(url)
    if r is not None and r.status_code == 200:
        print("Webhook invoked")
    else:
        print("Webhook failed")
        show_error()
        
def line_msg(token, message):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    } 
    params = {"message": message}
    from xrequests import post
    r = post("https://notify-api.line.me/api/notify",
                    params=params, headers=headers)  
    if r is not None and r.status_code == 200:
        print("Message sent...")
    else:
        print("Error! Failed to send notification message...")  
     
def pad_zero(v):
    if v < 10:
        return '0' + str(v)
    else:
        return str(v)
     
def format_datetime(local_time):
    Y,M,D,H,m,S,W,ds = local_time
    t = str(Y) + '-'
    t += pad_zero(M)
    t += '-'
    t += pad_zero(D)
    t += ' '
    t += pad_zero(H)
    t += ':'
    t += pad_zero(m)
    t += ':'
    t += pad_zero(S)
    return t