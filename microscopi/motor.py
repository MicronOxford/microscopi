import time
import os

from configobj import ConfigObj
import RPi.GPIO as GPIO

# Load config
config = ConfigObj('config.ini',unrepr=True)

PINS = config["motor"]["pins"]
MOTOR_STEPS = config["motor"]["steps"]
INIT_SPEED = config["motor"]["init_speed"]
ENDSTOP_PINS = config["motor"]["endstop_pins"]
MOTOR_STEP_TYPE = ["full", "full", "full"]
STEP_DELAY = 2e-6	# DRV8834 requires 1.9us minimum pulse

class Motor(object):
    def __init__(self, motor_id=0, name=None):
        self.id = motor_id

        if name is None:
            self.name = "motor"+str(motor_id)
        else:
            self.name = name

        self.setup()

    def setup(self):
        # Store initial motor settings
        self.direction = 1
        self.pins = PINS[self.id]
        self.base_steps = MOTOR_STEPS[self.id]
        self.speed = INIT_SPEED[self.id]
        self.endstop = ENDSTOP_PINS[self.id]

        # Init
        self.set_step_type(MOTOR_STEP_TYPE[self.id])
        self.set_speed(self.speed)
        self.set_busy(False)

        GPIO.setmode(GPIO.BCM)

        # Set all motor pins as outputs and to 0
        for key,val in self.pins.items():
            GPIO.setup(val, GPIO.OUT)
            GPIO.output(val, GPIO.LOW)

        # Initialise microswitch endstop GPIO pin
        if self.endstop is not None:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.endstop, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        print('Initialised  motor: '+str(self.id))

    def enable(self):
        pin = self.pins["SLEEP"]
        GPIO.output(pin,GPIO.HIGH)

    def disable(self):
        pin = self.pins["SLEEP"]
        GPIO.output(pin,GPIO.LOW)

    def set_busy(self,state):
        self.busy = state

    def get_endstop(self,motor_index = None):
        if self.endstop is None:
            return False
        else:
            return not GPIO.input(self.endstop)

    def set_speed(self,speed):
        # calculate motor delay
        self.base_delay = 60.0 / (speed * self.base_steps) # convert speed to revs/second and calculate delay between steps
        self.delay = self.base_delay / self.microsteps
        self.speed = speed

        # Sense-check delay time
        if(self.delay < .001):
            self.delay = .001
            self.speed = 60.0 / (self.base_steps * self.base_delay)
            print("Motor speed too fast, forcing speed to {}".format(self.speed))

    def set_direction(self,direction):
        self.direction = direction

    def set_step_type(self,step_type):
        # Set step type
        if(step_type == "full"):
            self.M0 = 0
            self.M1 = 0
            self.microsteps = 1

        elif(step_type == "half"):
            self.M0 = 1
            self.M1 = 0
            self.microsteps = 2

        elif(step_type == "micro-8"):
            self.M0 = 0
            self.M1 = 1
            self.microsteps = 8

        elif(step_type == "micro-16"):
            self.M0 = 1
            self.M1 = 1
            self.microsteps = 16

        else:
            step_type = "full"
            self.M0 = 0
            self.M1 = 0
            self.microsteps = 1

        self.n_steps = self.base_steps * self.microsteps
        self.step_type = step_type
        self.set_speed(self.speed)

    def _step(self):
        # Single pulse with minimum duration
        pin = self.pins["STEP"]
        GPIO.output(pin, GPIO.LOW)
        time.sleep(STEP_DELAY)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(STEP_DELAY)
        GPIO.output(pin, GPIO.LOW)

    def steps(self,n_steps,speed=None,direction=None,step_type=None):

        if(speed is not None):
            self.set_speed(speed)

        if(step_type is not None):
            self.set_step_type(step_type)

        if(direction is not None):
            self.set_direction(direction)
        else :
            # Set direction based on steps
            if(n_steps==0):
                pass
            elif(n_steps>0):
                self.set_direction(1)
            else:
                self.set_direction(0)

        # Set busy state
        self.set_busy(True)

        # Set direction
        GPIO.output(self.pins["DIR"],self.direction)

        # Perform steps
        print("Taking {} steps ({}) in the {} direction".format(n_steps,self.step_type,self.direction))

        for i in range(abs(n_steps)):
            if not (self.get_endstop() and not self.direction):
                self._step()
                time.sleep(self.delay)

        # Set busy state
        self.set_busy(False)


def get_motor(motor_number = 0):
    m = Motor(motor_number)
    return m
