
import camera
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

    camera.init()

    # wait for sensor to start and focus before capturing image
    await asyncio.sleep(2)
    buf = camera.capture()

    led.off()
    camera.deinit()

    if len(buf) > 0:
        yield from picoweb.start_response(resp, "image/jpeg")
        yield from resp.awrite(buf)
    else:
        picoweb.http_error(resp, 503)


def run():
    app.run(host='0.0.0.0', port=80, debug=True)
