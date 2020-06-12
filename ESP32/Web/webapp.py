
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
    app.run(host='192.168.1.105', port=80, debug=True)
