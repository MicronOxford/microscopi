import time
import os
import atexit

from configobj import ConfigObj
import pigpio

# Load config
config = ConfigObj('config.ini',unrepr=True)

# setup
LED_PIN = config["led"]["relay_pin"]
PWM_PIN = config["led"]["pwm_pin"]

pi = pigpio.pi()

def cleanup():
    pi.set_PWM_dutycycle(PWM_PIN, 0)

atexit.register(cleanup)

class LED(object):
    def __init__(self, relay_pin=LED_PIN, pwm_pin=PWM_PIN, brightness=50):
        self.relay_pin = relay_pin
        self.pwm_pin = pwm_pin
        self.pi = pigpio.pi()
        self.set_pwm_frequency(config["led"]["pwm_frequency"])
        self.set_pwm(brightness)

    def on(self):
        self.pi.write(self.relay_pin, 1)

    def off(self):
        self.pi.write(self.relay_pin, 0)

    def set_pwm(self, val):
        # Clamp within 0-100
        val = min(val,100)
        val = max(val,0)

        # Set pwm dutycycle
        self.pwm = val
        self.pi.set_PWM_dutycycle(self.pwm_pin, int(val/100*255))

        return val

    def set_pwm_frequency(self, frequency):
        self.pi.set_PWM_frequency(self.pwm_pin, frequency)

    def up(self, val=5):
        self.set_pwm(self.pwm+val)

    def down(self, val=5):
        self.set_pwm(self.pwm-val)
