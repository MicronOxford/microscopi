#!/usr/bin/python
import picamera
import thread
import motor

def input_thread(list):
	raw_input()
	list.append(None)

cam = picamera.PiCamera()
list = []
cam.start_preview()
thread.start_new_thread(input_thread, (list,))

try:
	motor.run_motor()

except KeyboardInterrupt:
	cam.stop_preview()
	exit()

