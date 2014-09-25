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
import time
import code
import pygame, sys
from pygame.locals import *

Cam = picamera.PiCamera() #create a camera object for controlling PiCamera
c = pygame.time.Clock() #create a clock object for timing 
pygame.init()
#code.interact(local=locals()) #creates interactive python shell for user inpu
w = 800
h = 600
size = (w,h)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Raspberry Pi Camera')
PREVIEW_TOGGLE = False

Cam.capture('image.jpg')
img=pygame.image.load('image.jpg')
screen.blit(img,(0,0))
c.tick(20) #ensure only three images per second max
Cam.capture('image.jpg')
print 'Image Captured'

#screen = pygame.display.set_mode(size)

# Initialize the joysticks
pygame.joystick.init()
# Constants representing the various buttons
#TODO Complete list, what about analog sensors?
DS_SELECT = 0
DS_ANALOG_LEFT = 1
DS_ANALOG_RIGHT = 2
DS_START = 3
DS_NORTH = 4
DS_WEST = 5
DS_SOUTH = 6
DS_EAST = 7
DS_TRIGGER_LEFT_2 = 8
DS_TRIGGER_RIGHT_2 = 9
DS_TRIGGER_LEFT_1 = 10
DS_TRIGGER_RIGHT_1 = 11
DS_TRIANGLE = 12
DS_CIRCLE = 13
DS_CROSS = 14
DS_SQUARE = 15
DS_PS = 16


# Ensure there are connected joysticks and init them
joystick_count = pygame.joystick.get_count()
for j in range(joystick_count):
    print 'Init joystick %s' % j
    joystick = pygame.joystick.Joystick(j)
    joystick.init()

def capture_image():
    Cam.capture('image.jpg')
    img=pygame.image.load('image.jpg')
    screen.blit(img, (0,0))
    print 'Image captured'

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                sys.exit()

	    	# if press 'p' on keyboard then toggle between
            # preview start and preview stop
            if event.key == K_p:   
                if PREVIEW_TOGGLE == False:
                    Cam.start_preview()
                    PREVIEW_TOGGLE = True
                elif PREVIEW_TOGGLE == True:
                    Cam.stop_preview()
                    PREVIEW_TOGGLE = False

            # if press 'c' on keybaord then capture image
            # save to file named image.jpg and display in pygame window 
            if event.key == K_c:    
                capture_image()
            if event.key == K_i:
                code.interact(local=locals()) # creates interactive python shell for 
                                              # user to control camera
        elif event.type == pygame.JOYBUTTONDOWN:
            print 'JoyButtonDown', event.button
            if event.button == DS_START:
                pygame.quit()
                sys.exit()
            elif event.button == DS_SQUARE:
                capture_image()

    pygame.display.flip()
    c.tick(20)

#    pygame.display.update()
#print 'doing stuff'
#testfunction = 'running function complete'
#def testcamera():
#    print testfunction

#testcamera 

#Cam.start_preview()
#sleep(10)
#Cam.stop_preview()
#DISPLAYSURF = pygame.display.set_mode((200, 150))
#pygame.display.set_caption('Raspberry Pi Camera')

#DISPLAYSURF = pygame.display.set_mode((200, 150))
#pygame.display.set_caption('Raspberry Pi Camera')

#WHITE = (255,255,255)
#BRACK = (0,0,0)
#GREEN = ( 0, 255, 0)
#RED = ( 255, 0, 0)

#DISPLAYSURF.fill(WHITE)
#pygame.draw.rect(DISPLAYSURF, GREEN, (100, 100, 200, 200))

