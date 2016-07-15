from Adafruit_MotorHAT import Adafruit_MotorHAT,Adafruit_StepperMotor 
import ps3 
import atexit 
import pygame 
from pygame.locals import *

DS_CROSS = 3

hat = Adafruit_MotorHAT()

def turnOffMotors():
	hat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	hat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	hat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	hat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

class Motor():
	def __init__(self,hat,stepper=1):
		self.hat = hat
		self.motor = self.hat.getStepper(200,1)
		self.motor.setSpeed(15)
		self.step_type = Adafruit_MotorHAT.DOUBLE


	def forward(self,steps=5):
		self.motor.step(steps, Adafruit_MotorHAT.FORWARD,self.step_type)

	def backward(self,steps=5):
		self.motor.step(steps,Adafruit_MotorHAT.BACKWARD,self.step_type)


def run_motor():
	motor = Motor(hat)
	
	pygame.init()
	screen = pygame.display.set_mode((100, 100))
	
	# init joystick
	pygame.joystick.init()
	for j in range(pygame.joystick.get_count()):
	    joystick = pygame.joystick.Joystick(j)
	    joystick.init()
	
	
	while True:
		for event in pygame.event.get():
			#Quit when q is pressed
                	keys = pygame.key.get_pressed()
                	if keys[K_q]:
                        	quit()

		j = pygame.joystick.Joystick(0)
		axis1 = joystick.get_axis(2)
	
		if axis1 > 0:
			motor.forward()
		elif axis1 < 0 :
			motor.backward()
		
	
		pygame.display.flip()

