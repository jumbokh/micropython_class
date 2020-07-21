
import picoweb
import machine
import time
import uasyncio as asyncio

led = machine.Pin(4, machine.Pin.OUT)
app = picoweb.WebApp('app')

import ulogging as logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('app')


@app.route('/')
def index(req, resp):

    # parse query string
    req.parse_qs()
    flash = req.form.get('flash', 'false')
    if flash == 'true':
        led.on()

    # wait for sensor to start and focus before capturing image
    await asyncio.sleep(2)

    led.off()

    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello World!")

def run():
<<<<<<< HEAD
    app.run(host='192.168.43.155', port=80, debug=True)
=======
    app.run(host='0.0.0.0', port=80, debug=True)
>>>>>>> 0310217171b2a9e9aa1b72531743a32736fe28ef
