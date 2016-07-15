import picamera
from wx.lib.pubsub import Publisher as pub
cam = picamera.PiCamera()
import menuv2

class Camera(object):
	def __init__(self):
		pub.subscribe(self.capture,"record")
		cam.preview_fullscreen = False
		cam.preview_window = (10,10, 610, 610)
		cam.zoom = (0.2, 0.2, 0.6, 0.6)
		cam.start_preview()

	def capture(self,message):
		nameNumberFileR = open("nameNumberFile")
		nameNumber = nameNumberFileR.read()
		self.cam.capture("image " + str(nameNumber) + ".png")
		nameNumber = nameNumber + 1 
		nameNumberFileW = open("nameNumberFile", "w")
		nameNumberFileW.write(nameNumber)

def Brightness(val1):
	cam.brightness = val1
	return val1

def Contrast(val2):	
		cam.contrast = val2
		return val2
		
def Exposure(val):	
		cam.exposure_compensation = val
		return val

def WB(val):
		cam.awb_mode = 'off'
		cam.awb_gains = (rg, bg)
		return (val)

#camera.awb_mode = 'off'
#rg, bg = (0.5, 0.5)
#camera.awb_gains = (rg, bg)
