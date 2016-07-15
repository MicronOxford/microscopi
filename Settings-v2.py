from wx import *
from wx.lib.pubsub import Publisher as pub

class B_and_C(wx.Frame):
		def __init__(self):
				wx.Frame.__init__(self, None, wx.ID_ANY, "Brightness and contrast tool", (0,25), wx.Size(500, 300))
				self.alphaValue = 255
				self.SetTransparent(self.alphaValue)
				panel = wx.Panel(self, -1)
				self.sld = wx.Slider(panel, -1, 200, 0, 100, wx.DefaultPosition, (250, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
				pub.sendMessage("brightness")

class Exposure(wx.Frame):
		def __init__(self):
				wx.Frame.__init__(self, None, wx.ID_ANY, "Exposure tool", (0,25), wx.Size(500, 300))
				self.alphaValue = 255
				self.SetTransparent(self.alphaValue)
				panel = wx.Panel(self, -1)
				self.sld = wx.Slider(panel, -1, 200, 0, 100, wx.DefaultPosition, (250, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
			 
class Zoom(wx.Frame):
		def __init__(self):
				wx.Frame.__init__(self, None, wx.ID_ANY, "Zoom tool", (0,25), wx.Size(500, 300))
				self.alphaValue = 255
				self.SetTransparent(self.alphaValue)
				panel = wx.Panel(self, -1)
				self.sld = wx.Slider(panel, -1, 200, 0, 100, wx.DefaultPosition, (250, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

class WhiteBalence(wx.Frame):
		def __init__(self):
				wx.Frame.__init__(self, None, wx.ID_ANY, "White Balence tool", (0,25), wx.Size(500, 300))
				self.alphaValue = 255
				self.SetTransparent(self.alphaValue)
				panel = wx.Panel(self, -1)
				self.sld = wx.Slider(panel, -1, 200, 0, 100, wx.DefaultPosition, (250, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

class Snapshot(wx.Frame):
		def __init__(self):
				nameNumberFileR = open("nameNumberFile")
				nameNumber = nameNumberFileR.read()
				self.cam.capture("image " + str(nameNumber) + ".png")
				nameNumber = nameNumber + 1 
				nameNumberFileW = open("nameNumberFile", "w")
				nameNumberFileW.write(nameNumber)

class Preview():
		def __init__(self):
				cam.stop_preview()

#class RecordV():
				#cam.start_recording()

class Stop(wx.Frame):
		def __init__(self):
				print "Please close the window"



