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

import picamera
from io import BytesIO
import time
import datetime
import pygame
import sys
from pygame.locals import *

# Import ps3 constants
from ps3 import *

# Import microscoPi settings
from settings import *

def now():
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

def toggle_preview(camera):
    # If there is no current preview, start preview
    if camera.preview is None:
        camera.start_preview(
            window=PREVIEW_LAYOUT,
            fullscreen=False)
    # Otherwise, stop preview
    else:
        camera.stop_preview()

def capture_image(camera):
    # Create byte stream to read image into
    stream = BytesIO()

    # Capture the image into the stream
    start = time.time()
    camera.capture(stream, format='jpeg')
    end = time.time()
    print 'capture', end - start

    # Return the acquired image stream
    stream.seek(0)
    return stream

def display_image(stream):
    # Seek to the start of the stream ready for reading
    stream.seek(0)
    
    # Load the image into pygame
    start = time.time()
    image = pygame.image.load(stream, 'jpeg')
    end = time.time()
    print 'pygame load', end - start

    # Get the current screen size of the pygame window to
    # correctly resize image
    screen_size = (pygame.display.Info().current_w,
                   pygame.display.Info().current_h)

    # Resize the image to the pygame window size
    start = time.time()
    image = pygame.transform.scale(image.convert(), screen_size)
    end = time.time()
    print 'scale', end - start

    # Display the image in the pygame window
    screen.blit(image, (0,0))

def save_image(stream, name):
    if stream is not None:
        open(name, 'wb').write(stream.getvalue())
    else:
        print('No image has been captured yet')

# Python interface to Raspberry Pi camera module
camera = picamera.PiCamera()

# Set the camera resolution to maximum for stills acquisition
camera.resolution = CAMERA_RESOLUTION

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Raspberry Pi Camera')

# To conserve resources, cap the framerate
c = pygame.time.Clock()
c.tick(MAX_FPS)

# Initialize the joysticks
pygame.joystick.init()

# Ensure there are connected joysticks and init them
joystick_count = pygame.joystick.get_count()
for j in range(joystick_count):
    joystick = pygame.joystick.Joystick(j)
    joystick.init()

# Global for most recently acquired image stream
timelapsing = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:

            # 'q' keypress - Quit
            if event.key == K_q:
                pygame.quit()
                sys.exit()

            # 'p' keypress - Toggle preview on/off
            elif event.key == K_p:   
                toggle_preview(camera)

            # 'c' keypress - Capture image
            elif event.key == K_c:    
                image_stream = capture_image(camera)
                save_image(image_stream, 'image.jpg')
                display_image(image_stream)

            # 't' keypress - Toggle timelapse
            elif event.key == K_t:
                if not timelapsing:
                    timelapsing = True
                    pygame.time.set_timer(USEREVENT + 1, TIMELAPSE_INTERVAL)
                else:
                    timelapsing = False
                    pygame.time.set_timer(USEREVENT + 1, 0)

            # 'i' keypress - Interactive Python Shell
            elif event.key == K_i:
                code.interact(local=locals())

        elif event.type == pygame.JOYBUTTONDOWN:
            print 'JoyButtonDown', event.button
            if event.button == DS_START:
                pygame.quit()
                sys.exit()
            elif event.button == DS_SQUARE:
                capture_image(camera)

        # Timelapse event, captured straight to disk
        elif event.type == USEREVENT + 1:
            stream = capture_image(camera)   
            save_image(stream, 'image-%s.jpg' % now())

    pygame.display.flip()

