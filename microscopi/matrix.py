from serial import Serial
import atexit

from configobj import ConfigObj

config = ConfigObj('config.ini', unrepr=True)

serial = Serial(config['matrix']['serial'])

def cleanup():
    serial.close()

atexit.register(cleanup)

class Matrix(object):
    def __init__(self):
        self._serial = serial
        self.init()
        self._brightness = 0

    def init(self):
        self._serial.write('set source matrix\n'.encode())

    def on(self):
        self._serial.write('on\n'.encode())

    def off(self):
        self._serial.write('off\n'.encode())

    def set_brightness(self, val):
        # Clamp within 0-15 and set to int
        val = min(val,15)
        val = max(val,0)
        val = int(val)

        # Set brightness
        self._brightness = val

        # Write to serial
        self._serial.write('set brightness {}\n'.format(val).encode())

        return val

    def send_command(self, val):
        self._serial.write('{}\n'.format(val).encode())

    def up(self, val=1):
        self.set_brightness(self._brightness+val)

    def down(self, val=1):
        self.set_brightness(self._brightness-val)
