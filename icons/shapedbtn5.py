# shapedBtnDemo.py Ilan Davis June 2016, based on tutorial on the web. 
# Icons made on iDraw (Graphic.app) on mac (in VSG format), saves as .png approx. 10%, 100pixes high. 
########################################################################
import wx
from wx.lib.agw.shapedbutton import SButton, SBitmapButton
from wx.lib.agw.shapedbutton import SBitmapToggleButton, SBitmapTextToggleButton

class MyForm(wx.Frame):
#----------------------------------------------------------------------
  def __init__(self):
    wx.Frame.__init__(self, None, wx.ID_ANY, "Cockpit V2.0", (0,25), wx.Size(800, 1200))
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
    bmpToggleTxtBtn3 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp3, label="", size=(75,75))
    bmpToggleTxtBtn3.Bind(wx.EVT_BUTTON, self.ToggleRedLaser)
    
    bmp4 = wx.Bitmap("icons/laser_farred_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn4 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp4, label="", size=(75,75))
    bmpToggleTxtBtn4.Bind(wx.EVT_BUTTON, self.ToggleFarredLaser)  

    bmp5 = wx.Bitmap("icons/laser_white_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn5 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp5, label="", size=(75,75))
    bmpToggleTxtBtn5.Bind(wx.EVT_BUTTON, self.ToggleWhiteLaser)  
    
    bmp6 = wx.Bitmap("icons/camera_blue_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn6 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp6, label="", size=(75,75))
    bmpToggleTxtBtn6.Bind(wx.EVT_BUTTON, self.ToggleCamera1)  
       
    bmp7 = wx.Bitmap("icons/camera_green_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn7 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp7, label="", size=(75,75))
    bmpToggleTxtBtn7.Bind(wx.EVT_BUTTON, self.ToggleCamera2)  
            
    bmp8 = wx.Bitmap("icons/camera_red_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn8 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp8, label="", size=(75,75))
    bmpToggleTxtBtn8.Bind(wx.EVT_BUTTON, self.ToggleCamera3)  
            
    bmp9 = wx.Bitmap("icons/camera_farred_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn9 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp9, label="", size=(75,75))
    bmpToggleTxtBtn9.Bind(wx.EVT_BUTTON, self.ToggleCamera4)  
    
    bmp10 = wx.Bitmap("icons/abort_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn10 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp10, label="", size=(75,75))
    bmpToggleTxtBtn10.Bind(wx.EVT_BUTTON, self.ToggleAbort)  
    
    bmp11 = wx.Bitmap("icons/capture_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn11 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp11, label="", size=(75,75))
    bmpToggleTxtBtn11.Bind(wx.EVT_BUTTON, self.ToggleCapture)  
      
    bmp12 = wx.Bitmap("icons/record_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn12 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp12, label="", size=(75,75))
    bmpToggleTxtBtn12.Bind(wx.EVT_BUTTON, self.ToggleCapture)  
      
    bmp13 = wx.Bitmap("icons/preview_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn13 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp13, label="", size=(75,75))
    bmpToggleTxtBtn13.Bind(wx.EVT_BUTTON, self.ToggleCapture)  
      
    bmp14 = wx.Bitmap("icons/snap_icon.png", wx.BITMAP_TYPE_ANY)
    bmpToggleTxtBtn14 = SBitmapTextToggleButton(panel, wx.ID_ANY, bitmap=bmp14, label="", size=(75,75))
    bmpToggleTxtBtn14.Bind(wx.EVT_BUTTON, self.ToggleSnap)  
    
    vbox = wx.BoxSizer(wx.VERTICAL)
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
