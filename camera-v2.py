import picamera
from wx.lib.pubsub import Publisher as pub


class Camera(object):
    def __init__(self):
		cam = picamera.PiCamera(0)
		cam.preview_fullscreen = False
		cam.preview_window = (200,200, 700, 700)
		cam.zoom = (0.2, 0.2, 0.6, 0.6)
		self.cam = cam
		pub.subscribe(self.capture,"capture")
		#pub.subscribe(self.capture,"record")
		#pub.subscribe(self.brightness ,"brightness") 
		cam.start_preview()
    	
def capture(self,message):
	nameNumberFileR = open("nameNumberFile")
	nameNumber = nameNumberFileR.read()
	self.cam.capture("image " + str(nameNumber) + ".png")
	nameNumber = nameNumber + 1 
	nameNumberFileW = open("nameNumberFile", "w")
	nameNumberFileW.write(nameNumber)

def brightness(self, brightness):
	cam.brightness = (self.sld,GetValue)	
		
		
