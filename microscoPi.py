#!/usr/bin/python
# microscoPi, Raspberry Pi based microscope platform
# Copyright (C) 2014 Ilan Davis, Mick Phillips & Douglas Russell
# University of Oxford, Oxford, United Kingdom
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#*******************************************************************************

# Import required libraries
import RPi.GPIO as GPIO
import picamera
from io import BytesIO
import datetime
import pygame
import sys
from pygame.locals import *

# Import ps3 constants
from ps3 import *

# Import microscoPi settings
from settings import *

# Use BCM GPIO references (naming convention for GPIO pins from Broadcom)
# instead of physical pin numbers on the Raspberry Pi board
GPIO.setmode(GPIO.BCM)

def now():
    """Get the current date and time"""
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

def toggle_preview(camera):
    """Toggle on/off the camera preview"""
    # If there is no current preview, start preview
    if camera.preview is None:
        camera.start_preview(
            window=PREVIEW_LAYOUT,
            fullscreen=False)
    # Otherwise, stop preview
    else:
        camera.stop_preview()

def capture_image(camera):
    """Capture an image into a stream in JPEG format"""
    # Create byte stream to read image into
    stream = BytesIO()

    # Capture the image into the stream
    camera.capture(stream, format='jpeg')

    # Return the acquired image stream
    stream.seek(0)
    return stream

def display_image(stream):
    """Display a captured stream in the pygame window"""
    # Seek to the start of the stream ready for reading
    stream.seek(0)

    # Load the image into pygame
    image = pygame.image.load(stream, 'jpeg')

    # Get the current screen size of the pygame window to
    # correctly resize image
    screen_size = (pygame.display.Info().current_w,
                   pygame.display.Info().current_h)

    # Resize the image to the pygame window size
    image = pygame.transform.scale(image.convert(), screen_size)

    # Display the image in the pygame window
    screen.blit(image, (0,0))


class Motor:
    """Motor control"""

    # Control sequence for these specific motors
    CONTROL_SEQUENCE = [[1,0,0,0],
                        [1,1,0,0],
                        [0,1,0,0],
                        [0,1,1,0],
                        [0,0,1,0],
                        [0,0,1,1],
                        [0,0,0,1],
                        [1,0,0,1]]

    def __init__(self, pins, wait_time=0.001, step_multiplier=50):
        """ Construct a Motor with the given pins and defaults"""
        # The pins that the specific motor is using
        self.pins = pins

        # Delay between motor steps
        # Change speed by changing the WAIT_TIME
        # Appropriate slower times are 0.5 or 0.01
        self.wait_time = wait_time

        # Number of steps to take per movement operation
        self.step_multiplier = step_multiplier

        # Setup the pins
        self.setup()

    # Setup pins
    def setup(self):
        """ Setup the pins for use"""
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

    def off(self):
        """ Turn the motor off"""
        for pin in self.pins:
            GPIO.output(pin, GPIO.LOW)

    # For backwards motion, supply a negative number of steps
    def move(self, wait_time=None, step_multiplier=None, reverse=False):
        """ Rotate the motor forwards/backwards"""
        # Use defaults for wait_time and step_multiplier if not specified
        if wait_time is None:
            wait_time = self.wait_time
        if step_multiplier is None:
            step_multiplier = self.step_multiplier

        # Adjust control sequence for direction
        if reverse:
            # Invert the control sequence list for reverse motion
            control_sequence = self.CONTROL_SEQUENCE[::-1]
        else:
            control_sequence = self.CONTROL_SEQUENCE

        # Move the motor a set number of steps
        for i in xrange(step_multiplier):
            # For each control sequence
            for control in control_sequence:
                # For each pin in the list of pin's to be set
                for pin in xrange(4):
                    GPIO.output(self.pins[pin], control[pin])
                # It is necessary to wait after each control sequence
                # The longer the wait, the slower the movement
                time.sleep(wait_time)

    def forward(self):
        """ Move forward at the default speed """
        self.move()

    def backward(self):
        """ Move forward at the default speed """
        self.move(None, None, True)


def save_image(stream, name):
    """ Same image to a specified file """
    if stream is not None:
        open(name, 'wb').write(stream.getvalue())
    else:
        print('No image has been captured yet')

def capture_save_display_image(camera, name):
    stream = capture_image(camera)
    save_image(stream, name)
    display_image(stream)

def quit():
    """ Quit application """
    # Cancels all GPIO setups and sets pins to GPIO.LOW
    pygaGPIO.cleanup()

    # Quit pygame
    pygame.quit()

    # Terminate program
    sys.exit()

# Python interface to Raspberry Pi camera module
camera = picamera.PiCamera()

# Set the camera resolution to maximum for stills acquisition
camera.resolution = CAMERA_RESOLUTION

# Initialise pygame
pygame.init()

# Set the size of the pygame display window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the caption of the pygame display window
pygame.display.set_caption('microscoPi')

# To conserve resources, cap the framerate
c = pygame.time.Clock()
c.tick(MAX_FPS)

# Initialise 'joystick' controller(s)
pygame.joystick.init()
for j in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(j)
    joystick.init()

# Setup motors with the specific pins used to control each
motorA = Motor([17,18,27,22])
motorB = Motor([23,24,25,04])

# Global for most recently acquired image stream
timelapsing = False

# Program loop, loops until quit
while True:
    # Handle any events that we are interested in
    for event in pygame.event.get():
        # Quit event, possibly fired by window controls
        if event.type == QUIT:
            quit()

        # Keypress events
        elif event.type == KEYDOWN:

            # 'q' keypress - Quit
            if event.key == K_q:
                quit()

            # 's' keypress - motor A forwards
            elif event.key == K_w:
                motorA.forward()

            # 'a' keypress - motor A Backwards
            elif event.key == K_s:
                motorA.backward()

            # 'z' keypress - motor B forwards
            elif event.key == K_a:
                motorB.forward()

            # 'w' keypress - motor B Backwards
            elif event.key == K_d:
                motorB.backward()

            # 'h' keypress - Set motors to high speed motion
            elif event.key == K_h:
                motorA.step_multiplier = 50
                motorB.step_multiplier = 50

            # 'm' keypress - Set motors to medium speed motion
            elif event.key == K_m:
                motorA.step_multiplier = 20
                motorB.step_multiplier = 20

            # 'l' keypress - Set motors to low speed motion
            elif event.key == K_l:
                motorA.step_multiplier = 1
                motorB.step_multiplier = 1

            # 'p' keypress - Toggle preview on/off
            elif event.key == K_p:
                toggle_preview(camera)

            # 'c' keypress - Capture image
            elif event.key == K_c:
            capture_save_display_image(camera, 'image.jpg')

            # 't' keypress - Toggle timelapse
            elif event.key == K_t:
                if not timelapsing:
                    timelapsing = True
                    pygame.time.set_timer(USEREVENT + 1, TIMELAPSE_INTERVAL)
                else:
                    timelapsing = False
                    pygame.time.set_timer(USEREVENT + 1, 0)

            # 'i' keypress - Interactive Python Shell
            #elif event.key == K_i:
            #    code.interact(local=locals())

        #Joystick events
        elif event.type == pygame.JOYBUTTONDOWN:
            # print 'JoyButtonDown', event.button

            # 'Start' button - Quit
            if event.button == DS_START:
                quit()

            # 'Square' button - capture, save and display image
            elif event.button == DS_SQUARE:
                capture_save_display_image(camera, 'image.jpg')

        # Timelapse event, captured straight to disk
        elif event.type == USEREVENT + 1:
            stream = capture_image(camera)
            save_image(stream, 'image-%s.jpg' % now())

    # Read and react to joystick movement outside of the event handler
    joystick = pygame.joystick.Joystick(0)
    axis0 = joystick.get_axis(0)
    # axis1 = joystick.get_axis(1)
    axis2 = joystick.get_axis(2)
    # axis3 = joystick.get_axis(3)

    # Adjust movement speed based on analogue input and move
    # the motor in the direction indicated
    if axis0 != 0:
        if abs(axis0) > 0.9:
            wait_time = 0.001
        elif abs(axis0) > 0.5:
            wait_time = 0.008
        elif abs(axis0) > 0:
            wait_time = 0.01

        if axis0 > 0:
            motorA.move(wait_time)
        elif axis0 < 0:
            motorA.move(wait_time, None, True)

    if axis2 != 0:
        if abs(axis2) > 0.9:
            wait_time = 0.001
        elif abs(axis2) > 0.5:
            wait_time = 0.008
        elif abs(axis2) > 0:
            wait_time = 0.06

        if axis2 > 0:
            motorB.move(wait_time)
        elif axis2 < 0:
            motorB.move(wait_time, None, True)

    pygame.display.flip()
