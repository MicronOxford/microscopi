#!/usr/bin/python
import pygame
import thread
import motor
import numpy
import time
import menuv2
import wx
import camerav2
from wx.lib.pubsub import Publisher as pub


def menu():
    myform = menuv2.MyForm()
    myform.Show()
    app.MainLoop()
  
pygame.init()


app = wx.App(False)
thread.start_new_thread(menu,tuple())
thread.start_new_thread(camerav2.Camera,tuple())



for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.JOYBUTTONDOWN:
                if event.button == DS_TRIGGER_RIGHT_2:
                         pub.sendMessage("capture",[])
                elif event.button == DS_TRIGGER_RIGHT_1:
                         pub.sendMessage("record")
                #elif
    


try:
        motor.run_motor()

except KeyboardInterrupt:
        exit()

