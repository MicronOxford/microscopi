# shapedBtnDemo.py Ilan Davis June 2016, based on tutorial on the web. 
# Icons made on iDraw (Graphic.app) on mac (in VSG format), saves as .png approx. 10%, 100pixes high. 
########################################################################
import wx
from wx.lib.agw.shapedbutton import SButton, SBitmapButton
from wx.lib.agw.shapedbutton import SBitmapToggleButton, SBitmapTextToggleButton

class MyForm(wx.Frame):
#----------------------------------------------------------------------
  def __init__(self):
    wx.Frame.__init__(self, None, wx.ID_ANY, "Cockpit V2.0", (0,25), wx.Size(700, 600))
    self.alphaValue = 255
    self.SetTransparent(self.alphaValue)
    panel = wx.Panel(self, wx.ID_ANY)

    bmp1 = wx.Bitmap("icons/laser_blue_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn1 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp1, label="", size=(100,100))
    bmpToggleTxtBtn1.Bind(wx.EVT_BUTTON, self.ToggleBlueLaser)
    
    bmp2 = wx.Bitmap("icons/laser_green_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn2 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp2, label="", size=(100,100))
    bmpToggleTxtBtn2.Bind(wx.EVT_BUTTON, self.ToggleGreenLaser)
 
    bmp3 = wx.Bitmap("icons/laser_red_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn3 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp3, label="", size=(100,100))
    bmpToggleTxtBtn3.Bind(wx.EVT_BUTTON, self.ToggleRedLaser)
    
    bmp4 = wx.Bitmap("icons/laser_farred_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn4 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp4, label="", size=(100,100))
    bmpToggleTxtBtn4.Bind(wx.EVT_BUTTON, self.ToggleFarredLaser)  

    bmp5 = wx.Bitmap("icons/laser_white_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn5 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp5, label="", size=(100,100))
    bmpToggleTxtBtn5.Bind(wx.EVT_BUTTON, self.ToggleWhiteLaser)  
    
    bmp6 = wx.Bitmap("icons/camera_blue_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn6 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp6, label="", size=(100,100))
    bmpToggleTxtBtn6.Bind(wx.EVT_BUTTON, self.ToggleCamera1)  
       
    bmp7 = wx.Bitmap("icons/camera_green_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn7 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp7, label="", size=(100,100))
    bmpToggleTxtBtn7.Bind(wx.EVT_BUTTON, self.ToggleCamera2)  

    bmp8 = wx.Bitmap("icons/camera_red_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn8 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp8, label="", size=(100,100))
    bmpToggleTxtBtn8.Bind(wx.EVT_BUTTON, self.ToggleCamera3)  
            
    bmp9 = wx.Bitmap("icons/camera_farred_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn9 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp9, label="", size=(100,100))
    bmpToggleTxtBtn9.Bind(wx.EVT_BUTTON, self.ToggleCamera4)  
    
    bmp10 = wx.Bitmap("icons/abort_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn10 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp10, label="", size=(100,100))
    bmpToggleTxtBtn10.Bind(wx.EVT_BUTTON, self.ToggleAbort)  
    
    bmp11 = wx.Bitmap("icons/capture_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn11 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp11, label="", size=(100,100))
    bmpToggleTxtBtn11.Bind(wx.EVT_BUTTON, self.ToggleCapture)  
      
    bmp12 = wx.Bitmap("icons/record_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn12 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp12, label="", size=(100,100))
    bmpToggleTxtBtn12.Bind(wx.EVT_BUTTON, self.ToggleCapture)  
      
    bmp13 = wx.Bitmap("icons/preview_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn13 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp13, label="", size=(100,100))
    bmpToggleTxtBtn13.Bind(wx.EVT_BUTTON, self.ToggleCapture)  
      
    bmp14 = wx.Bitmap("icons/snap_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn14 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp14, label="", size=(100,100))
    bmpToggleTxtBtn14.Bind(wx.EVT_BUTTON, self.ToggleSnap)  
    
    bmp15 = wx.Bitmap("icons/camera_red_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn15 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp15, label="", size=(100,100))
    bmpToggleTxtBtn15.Bind(wx.EVT_BUTTON, self.ToggleCamera3)  
            
    bmp16 = wx.Bitmap("icons/camera_farred_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn16 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp16, label="", size=(100,100))
    bmpToggleTxtBtn16.Bind(wx.EVT_BUTTON, self.ToggleCamera4)  
    
    bmp17 = wx.Bitmap("icons/abort_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn17 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp17, label="", size=(100,100))
    bmpToggleTxtBtn17.Bind(wx.EVT_BUTTON, self.ToggleAbort)  
    
    bmp18 = wx.Bitmap("icons/capture_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn18 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp18, label="", size=(100,100))
    bmpToggleTxtBtn18.Bind(wx.EVT_BUTTON, self.ToggleCapture)  
      
    bmp19 = wx.Bitmap("icons/record_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn19 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp19, label="", size=(100,100))
    bmpToggleTxtBtn19.Bind(wx.EVT_BUTTON, self.ToggleCapture)  
      
    bmp20 = wx.Bitmap("icons/preview_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn20 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp20, label="", size=(100,100))
    bmpToggleTxtBtn20.Bind(wx.EVT_BUTTON, self.ToggleCapture)  
      
    bmp21 = wx.Bitmap("icons/snap_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn21 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp21, label="", size=(100,100))
    bmpToggleTxtBtn21.Bind(wx.EVT_BUTTON, self.ToggleSnap)  
      
    bmp22 = wx.Bitmap("icons/preview_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn22 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp22, label="", size=(100,100))
    bmpToggleTxtBtn22.Bind(wx.EVT_BUTTON, self.ToggleCapture)  
      
    bmp23 = wx.Bitmap("icons/snap_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn23 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp23, label="", size=(100,100))
    bmpToggleTxtBtn23.Bind(wx.EVT_BUTTON, self.ToggleSnap)  
    
    bmp24 = wx.Bitmap("icons/camera_red_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn24 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp24, label="", size=(100,100))
    bmpToggleTxtBtn24.Bind(wx.EVT_BUTTON, self.ToggleCamera3)  
            
    bmp25 = wx.Bitmap("icons/camera_farred_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn25 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp25, label="", size=(100,100))
    bmpToggleTxtBtn25.Bind(wx.EVT_BUTTON, self.ToggleCamera4)  
    
    bmp26 = wx.Bitmap("icons/abort_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn26 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp26, label="", size=(100,100))
    bmpToggleTxtBtn26.Bind(wx.EVT_BUTTON, self.ToggleAbort)  
    
    bmp27 = wx.Bitmap("icons/capture_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn27 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp27, label="", size=(100,100))
    bmpToggleTxtBtn27.Bind(wx.EVT_BUTTON, self.ToggleCapture)  
      
    bmp28 = wx.Bitmap("icons/record_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn28 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp28, label="", size=(100,100))
    bmpToggleTxtBtn28.Bind(wx.EVT_BUTTON, self.ToggleCapture)  
      
    bmp29 = wx.Bitmap("icons/preview_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn29 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp29, label="", size=(100,100))
    bmpToggleTxtBtn29.Bind(wx.EVT_BUTTON, self.ToggleCapture)  
      
    bmp30 = wx.Bitmap("icons/snap_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn30 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp30, label="", size=(100,100))
    bmpToggleTxtBtn30.Bind(wx.EVT_BUTTON, self.ToggleSnap)  
    
    vbox = wx.GridSizer(5,6,3,3)  #Layout the buttons in a 2D array of 7x3
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
  def ToggleBlueLaser(self, event):
    if event.GetIsDown():
      print "Blue Laser is ON"
    else:
      print "Blue Laser is OFF"
    event.Skip()   
#----------------------------------------------------------------------
  def ToggleGreenLaser(self, event):
    if event.GetIsDown():
      print "Green Laser is ON"
    else:
      print "Green Laser is OFF"
    event.Skip()  
#----------------------------------------------------------------------
  def ToggleRedLaser(self, event):
    if event.GetIsDown():
      print "Red Laser is ON"
    else:
      print "Red Laser is OFF"
    event.Skip()   
#----------------------------------------------------------------------
  def ToggleFarredLaser(self, event):
    if event.GetIsDown():
      print "Far Red Laser is ON"
    else:
      print "Far Red Laser is OFF"
    event.Skip()
#----------------------------------------------------------------------
  def ToggleWhiteLaser(self, event):
    if event.GetIsDown():
      print "White Laser is ON"
    else:
      print "Far Red Laser is OFF"
    event.Skip()
#----------------------------------------------------------------------
  def ToggleCamera1(self, event):
    if event.GetIsDown():
      print "Camera1 is ON"
    else:
      print "Camera1 is OFF"
    event.Skip()
#----------------------------------------------------------------------
  def ToggleCamera2(self, event):
    if event.GetIsDown():
      print "Camera2 is ON"
    else:
      print "Camera2 is OFF"
    event.Skip()
#----------------------------------------------------------------------
  def ToggleCamera3(self, event):
    if event.GetIsDown():
      print "Camera3 is ON"
    else:
      print "Camera3 is OFF"
    event.Skip()
#----------------------------------------------------------------------
  def ToggleCamera4(self, event):
    if event.GetIsDown():
      print "Camera4 is ON"
    else:
      print "Camera4 is OFF"
    event.Skip()
#----------------------------------------------------------------------
  def ToggleAbort(self, event):
    if event.GetIsDown():
      print "Abort Requested"
    else:
      print "Abort button is reset to OFF"
    event.Skip()
#----------------------------------------------------------------------
  def ToggleCapture(self, event):
    if event.GetIsDown():
      print "Capture experiment started"
    else:
      print "Capture experiment stopped"
    event.Skip()
#----------------------------------------------------------------------
  def ToggleRecord(self, event):
    if event.GetIsDown():
      print "Capture experiment started"
    else:
      print "Capture experiment stopped"
    event.Skip()
#----------------------------------------------------------------------
  def TogglePreview(self, event):
    if event.GetIsDown():
      print "Capture experiment started"
    else:
      print "Capture experiment stopped"
    event.Skip()
#----------------------------------------------------------------------    
  def ToggleSnap(self, event):
    if event.GetIsDown():
      print "Capture experiment started"
    else:
      print "Capture experiment stopped"
    event.Skip()
#----------------------------------------------------------------------
    
#  def onShapedBtn(self, event):
#    self.showDialog("You Pressed the Normal ShapedButton!")
#----------------------------------------------------------------------
#  def showDialog(self, message):    #Displays a custom message
#    dlg = wx.MessageDialog(None, message, 'Message', wx.OK|wx.ICON_EXCLAMATION)
#    dlg.ShowModal()
#    dlg.Destroy()

# Run the program
if __name__ == "__main__":
  app = wx.App(False)
  frame = MyForm()
  frame.Show()
  app.MainLoop()

