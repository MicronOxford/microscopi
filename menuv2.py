'''2Dmenu-v1.py Ollie Pope's July 2016 modification of Ilan Davis June 2016, 2D array of icon
menu in wxpython to select with PS3 controller as front GUI end of microscope controller setup
on motic.  based on tutorial on the web. 
Icons made on iDraw (Graphic.app) on mac (in VSG format), saves as .png approx. 10%, 100pixes high.''' 
########################################################################
import wx
from wx.lib.agw.shapedbutton import SButton, SBitmapButton
from wx.lib.agw.shapedbutton import SBitmapToggleButton, SBitmapTextToggleButton
import Settings

class MyForm(wx.Frame):
#----------------------------------------------------------------------
		def __init__(self):
				wx.Frame.__init__(self, None, wx.ID_ANY, "Ollie Pope's microscope interface V1.0", (0,25), wx.Size(700, 600))
				self.alphaValue = 255
				self.SetTransparent(self.alphaValue)
				panel = wx.Panel(self, wx.ID_ANY)

				bmp1 = wx.Bitmap("icons/Brightness and contrast.png", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn1 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp1, label="", size=(100,100))
				bmpToggleTxtBtn1.Bind(wx.EVT_BUTTON, self.BrightnessAndContrast)
		
				bmp2 = wx.Bitmap("icons/exposure.png", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn2 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp2, label="", size=(100,100))
				bmpToggleTxtBtn2.Bind(wx.EVT_BUTTON, self.Exposure)
			 
				bmp3 = wx.Bitmap("icons/Zoom.png", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn3 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp3, label="", size=(100,100))
				bmpToggleTxtBtn3.Bind(wx.EVT_BUTTON, self.Zoom)
		
				bmp4 = wx.Bitmap("icons/whitebalence.png", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn4 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp4, label="", size=(100,100))
				bmpToggleTxtBtn4.Bind(wx.EVT_BUTTON, self.WhiteBalence)  

				bmp5 = wx.Bitmap("icons/capture_icon.png", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn5 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp5, label="", size=(100,100))
				bmpToggleTxtBtn5.Bind(wx.EVT_BUTTON, self.Capture)  
		
				bmp6 = wx.Bitmap("icons/preview_icon.png", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn6 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp6, label="", size=(100,100))
				bmpToggleTxtBtn6.Bind(wx.EVT_BUTTON, self.Preview)  
				   
				bmp7 = wx.Bitmap("icons/record_icon.png", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn7 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp7, label="", size=(100,100))
				bmpToggleTxtBtn7.Bind(wx.EVT_BUTTON, self.Record)  

				bmp8 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn8 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap = bmp8, label="", size=(100,100))
				bmpToggleTxtBtn8.Bind(wx.EVT_BUTTON, self.Nothing1)  
						
				bmp9 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn9 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap = bmp9,  label="", size=(100,100))
				bmpToggleTxtBtn9.Bind(wx.EVT_BUTTON, self.Nothing2)  
		
				bmp10 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn10 = SBitmapTextToggleButton(panel, wx.ID_ANY,  bitmap = bmp10,  label="", size=(100,100))
				bmpToggleTxtBtn10.Bind(wx.EVT_BUTTON, self.Nothing3)  
		
				bmp11 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn11 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap = bmp11,  label="", size=(100,100))
				bmpToggleTxtBtn11.Bind(wx.EVT_BUTTON, self.Nothing4)  
				  
				bmp12 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn12 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap = bmp12,  label="", size=(100,100))
				bmpToggleTxtBtn12.Bind(wx.EVT_BUTTON, self.Nothing5)  
				  
				bmp13 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn13 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap = bmp13,  label="", size=(100,100))
				bmpToggleTxtBtn13.Bind(wx.EVT_BUTTON, self.Nothing6)  
				  
				bmp14 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn14 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp14, label="", size=(100,100))
				bmpToggleTxtBtn14.Bind(wx.EVT_BUTTON, self.Nothing7)  
		
				bmp15 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn15 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp15, label="", size=(100,100))
				bmpToggleTxtBtn15.Bind(wx.EVT_BUTTON, self.Nothing8)  
						
				bmp16 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn16 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp16, label="", size=(100,100))
				bmpToggleTxtBtn16.Bind(wx.EVT_BUTTON, self.Nothing9)  
		
				bmp17 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn17 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp17, label="", size=(100,100))
				bmpToggleTxtBtn17.Bind(wx.EVT_BUTTON, self.Nothing10)  
		
				bmp18 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn18 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp18, label="", size=(100,100))
				bmpToggleTxtBtn18.Bind(wx.EVT_BUTTON, self.Nothing11)  
				  
				bmp19 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn19 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp19, label="", size=(100,100))
				bmpToggleTxtBtn19.Bind(wx.EVT_BUTTON, self.Nothing12)  
				  
				bmp20 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn20 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp20, label="", size=(100,100))
				bmpToggleTxtBtn20.Bind(wx.EVT_BUTTON, self.Nothing13)  
				  
				bmp21 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn21 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp21, label="", size=(100,100))
				bmpToggleTxtBtn21.Bind(wx.EVT_BUTTON, self.Nothing14)  
				  
				bmp22 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn22 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp22, label="", size=(100,100))
				bmpToggleTxtBtn22.Bind(wx.EVT_BUTTON, self.Nothing15)  
				  
				bmp23 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn23 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp23, label="", size=(100,100))
				bmpToggleTxtBtn23.Bind(wx.EVT_BUTTON, self.Nothing16)  
		
				bmp24 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn24 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp24, label="", size=(100,100))
				bmpToggleTxtBtn24.Bind(wx.EVT_BUTTON, self.Nothing17)  
			  
				bmp25 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn25 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp25, label="", size=(100,100))
				bmpToggleTxtBtn25.Bind(wx.EVT_BUTTON, self.Nothing18)  
		
				bmp26 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn26 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp26, label="", size=(100,100))
				bmpToggleTxtBtn26.Bind(wx.EVT_BUTTON, self.Nothing19)  
		
				bmp27 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn27 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp27, label="", size=(100,100))
				bmpToggleTxtBtn27.Bind(wx.EVT_BUTTON, self.Nothing20)  
				  
				bmp28 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn28 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp28, label="", size=(100,100))
				bmpToggleTxtBtn28.Bind(wx.EVT_BUTTON, self.Nothing21)  
				  
				bmp29 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn29 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp29, label="", size=(100,100))
				bmpToggleTxtBtn29.Bind(wx.EVT_BUTTON, self.Nothing22)  
				  
				bmp30 = wx.Bitmap("", wx.BITMAP_TYPE_ANY)
				bmpToggleTxtBtn30 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp30, label="", size=(100,100))
				bmpToggleTxtBtn30.Bind(wx.EVT_BUTTON, self.Nothing23)  
    
				vbox = wx.GridSizer(5,6,3,3)  #Layout the buttons in a 2D array of 5x6 mnimum spacing around each icon of 3x3 pixels

				vbox.Add(bmpToggleTxtBtn1, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn2, 0, wx.ALL, wx.CENTER, 5) 
				vbox.Add(bmpToggleTxtBtn3, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn4, 0, wx.ALL, wx.CENTER, 5)   
				vbox.Add(bmpToggleTxtBtn5, 0, wx.ALL, wx.CENTER, 5) 
		
				vbox.Add(bmpToggleTxtBtn6, 0, wx.ALL, wx.CENTER, 5) 
				vbox.Add(bmpToggleTxtBtn7, 0, wx.ALL, wx.CENTER, 5)     
				vbox.Add(bmpToggleTxtBtn8, 0, wx.ALL, wx.CENTER, 5) 
				vbox.Add(bmpToggleTxtBtn9, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn10, 0, wx.ALL, wx.CENTER, 5)
		
				vbox.Add(bmpToggleTxtBtn11, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn12, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn13, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn14, 0, wx.ALL, wx.CENTER, 5)    
				vbox.Add(bmpToggleTxtBtn15, 0, wx.ALL, wx.CENTER, 5) 
		
				vbox.Add(bmpToggleTxtBtn16, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn17, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn18, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn19, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn20, 0, wx.ALL, wx.CENTER, 5)
		
				vbox.Add(bmpToggleTxtBtn21, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn22, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn23, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn24, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn25, 0, wx.ALL, wx.CENTER, 5)
		
				vbox.Add(bmpToggleTxtBtn26, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn27, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn28, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn29, 0, wx.ALL, wx.CENTER, 5)
				vbox.Add(bmpToggleTxtBtn30, 0, wx.ALL, wx.CENTER, 5)

				panel.SetSizer(vbox)
		
#----------------------------------------------------------------------
		def BrightnessAndContrast(self, event):
				if event.GetIsDown():
		  				#create new window with sliders for brightness and contrast
						BandC = Settings.B_and_C()
		  				print "Brightness and contrast tool is ON"
						BandC.Show()
				else:
		  				print "Brightness and contrast tool is OFF"
						stop = Settings.Stop()
						stop.Show()
						event.Skip()   
#----------------------------------------------------------------------
		def Exposure(self, event):
				if event.GetIsDown():
		  			    #create new window with sliders for brightness and contrast
						exposure = Settings.Exposure()
						print "Exposure tool is ON"
						exposure.Show()
				else:
		  				print "Exposure tool is OFF"
						stop = Settings.Stop()
						stop.Show()
						event.Skip()   
#----------------------------------------------------------------------
		def Zoom(self, event):
				if event.GetIsDown():
		  				#create new window with sliders for zoom
						zoom = Settings.Zoom()
		  				print "Zoom tool is ON"
						zoom.Show()
				else:
		  				print "Zoom tool is OFF"
						stop = Settings.Stop()
						stop.Show()
						event.Skip()  
#----------------------------------------------------------------------
		def WhiteBalence(self, event):
				if event.GetIsDown():
		  				#create new window with sliders for white balence
						WB = Settings.WhiteBalence()
		  				print "White balence tool is ON"
						WB.Show()
				else:
		  				print "White balence tool is OFF"
						stop = Settings.Stop()
						stop.Show()
						event.Skip()   
#----------------------------------------------------------------------
		def Capture(self, event):
				if event.GetIsDown():
		  				print "Image is being captured"
		  				#capture an image
						Snap = Settings.Snapshot()
						Snap.Show()
				else:
		  				pass
						event.Skip()
#----------------------------------------------------------------------
		def Preview(self, event):
				if event.GetIsDown():
		  				print "Preview is ON"
		  				#toggle the preview window
						Prev = Settings.Preview()
						Prev.Show()
				else:
		  				print "Preview is OFF"
						event.Skip()
#----------------------------------------------------------------------
		def Record(self, event):
				if event.GetIsDown():
		  				print "Recording has started"
		  				#record a video
						#Rec = Settings.RecordV()
						#Rec.Show()
				else:
		  				print "Recording has stopped"
						#event.Skip()
#----------------------------------------------------------------------
		def Nothing1(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------
		def Nothing2(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------
		def Nothing3(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------
		def Nothing4(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------
		def Nothing5(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------
		def Nothing6(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Buttton is OFF"
						event.Skip()
#----------------------------------------------------------------------
		def Nothing7(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------    
		def Nothing8(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing9(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing10(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing11(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing12(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing13(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing14(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing15(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing16(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing17(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing18(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing19(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing20(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing21(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing22(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

		def Nothing23(self, event):
				if event.GetIsDown():
		  				print "This button has no value"
				else:
		  				print "Button is OFF"
						event.Skip()
#----------------------------------------------------------------------

# Run the program
if __name__ == "__main__":
  app = wx.App(False)
  frame = MyForm()
  frame.Show()
  app.MainLoop()


