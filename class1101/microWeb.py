import picoweb
from time import sleep
from machine import Pin
from dht import DHT11
import network
import config
import time
#https://www.fooish.com/html/table.html
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
  print('connecting to network...')
  sta_if.active(True)
  sta_if.connect(config.SSID, config.KEY)
  while not sta_if.isconnected():
    pass
print('network config:', sta_if.ifconfig())
ipadd=sta_if.ifconfig()

def getTime():
    now = time.time()
    t = time.localtime(now)
    d = "{}-{}-{} {}:{}:{}".format(t[0],t[1],t[2],t[3],t[4],t[5])
    print(d)
    return [t[3],t[4]]
[H,S] = getTime()    
app = picoweb.WebApp(__name__)
hw_sensor=DHT11(Pin(13,Pin.IN,Pin.PULL_UP))
  
@app.route("/")
def hello(req, resp): 
    yield from picoweb.start_response(resp) 
    yield from resp.awrite("Hello World!")

@app.route("/temp")
def html(req, resp):
    hw_sensor.measure()
    t = hw_sensor.temperature()
    h = hw_sensor.humidity()
    sensor={"tmpr":t,"hmdty":h }
    tstamp = {"Hour":H, "Second":S}
    msg = (b'{0:3.1f} {1:3.1f} {2:2d}:{3:2d}'.format(t,h,H,S))
    print(msg)
    yield from picoweb.start_response(resp, content_type = "text/html")
    yield from app.render_template(resp, "sensor_tpl", (sensor,tstamp))
app.run(debug=True, host =ipadd[0])