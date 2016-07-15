from wx import *
from wx.lib.pubsub import Publisher as pub
import camera
import time

class B_and_C(wx.Frame):
		def __init__(self):
				wx.Frame.__init__(self, None, wx.ID_ANY, "Brightness and contrast tool", (0,25), wx.Size(500, 300))
				vbox = wx.BoxSizer(wx.VERTICAL)
				hbox = wx.BoxSizer(wx.HORIZONTAL)
				self.alphaValue = 240
				self.SetTransparent(self.alphaValue)
				panel = wx.Panel(self, -1)
				self.sld1 = wx.Slider(panel, -1, 200, 0, 100, wx.DefaultPosition, (250, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
				self.sld2 = wx.Slider(panel, -1, 200, 0, 100, wx.DefaultPosition, (250, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
				btn1 = wx.Button(panel, 8, 'Adjust brightness')
				btn3 = wx.Button(panel, 7, 'Adjust contrast')
				btn2 = wx.Button(panel, 9, 'Close')
				wx.EVT_BUTTON(self, 8, self.OnAdjust1)
				wx.EVT_BUTTON(self, 7, self.OnAdjust2)
				wx.EVT_BUTTON(self, 9, self.OnClose)
				hbox.Add(btn1, 1, wx.RIGHT, 10)
				hbox.Add(btn2, 1)
				hbox.Add(btn3, 1, wx.ALIGN_CENTRE, 10 )
				vbox.Add(hbox, 0, wx.ALIGN_CENTRE | wx.ALL, 20)
				vbox.Add(self.sld1, 1, wx.ALIGN_CENTRE)
				vbox.Add(self.sld2, 1, wx.ALIGN_CENTRE)
				panel.SetSizer(vbox)

		def OnAdjust1(self, event):
				val1 = self.sld1.GetValue()
				camera.Brightness(val1)
		
		def OnAdjust2(self, event):
				val2 = self.sld2.GetValue()
				camera.Contrast(val2)
  
  		def OnClose(self, event):
      			self.Close()
					

class Exposure(wx.Frame):
		def __init__(self):
				wx.Frame.__init__(self, None, wx.ID_ANY, "Exposure tool", (0,25), wx.Size(500, 300))
				vbox = wx.BoxSizer(wx.VERTICAL)
				hbox = wx.BoxSizer(wx.HORIZONTAL)
				self.alphaValue = 240
				self.SetTransparent(self.alphaValue)
				panel = wx.Panel(self, -1)
				self.sld = wx.Slider(panel, -1, 200, -25, 25, wx.DefaultPosition, (250, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
				btn1 = wx.Button(panel, 8, 'Adjust exposure')
				btn2 = wx.Button(panel, 9, 'Close')
				wx.EVT_BUTTON(self, 8, self.OnAdjust)
				wx.EVT_BUTTON(self, 9, self.OnClose)
				hbox.Add(btn1, 1, wx.RIGHT, 10)
				hbox.Add(btn2, 1)
				vbox.Add(hbox, 0, wx.ALIGN_CENTRE | wx.ALL, 20)
				vbox.Add(self.sld, 1, wx.ALIGN_CENTRE)
				panel.SetSizer(vbox)

		def OnAdjust(self, event):
				val = self.sld.GetValue()
				camera.Exposure(val)

		def OnClose(self, event):
      			self.Close()
			 
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



