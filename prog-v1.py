#!/usr/bin/python
import pygame
import picamera
import thread
import motor
import numpy
import time

def input_thread(list):
	raw_input()
	list.append(None)

pygame.init()
cam = picamera.PiCamera()
list = []
cam.preview_fullscreen = False
cam.preview_window = (200,200, 700, 700)
cam.zoom = (0.2, 0.2, 0.6, 0.6)
cam.start_preview()

for event in pygame.event.get():
	keys = pygame.key.get_pressed()
      	if event.type == pygame.JOYBUTTONDOWN:
		if event.button == DS_TRIGGER_RIGHT_2:
			cam.capture('image.jpg')

thread.start_new_thread(input_thread, (list,))

try:
	motor.run_motor()

except KeyboardInterrupt:
	cam.stop_preview()
	exit()
