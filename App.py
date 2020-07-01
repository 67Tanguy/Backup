#!/usr/bin/env python

import wx
import wx.svg
import GUI.Frame as Frame
import wx.lib.buttons as buts
import os

def folderChoice():
    selector = wx.DirSelector("choose a folder")
    return selector

# create the app
app = wx.App()

#create the frame with min and max size
frm = Frame.Frame(None, title='Backup',size=(1080,720))
frm.Show()
frm.Title = "Backup"

#create a panel 
panel = wx.Panel(frm)
panel.SetSize(frm.GetSize())

# create two buttons 
button = wx.Button(panel, label="Choose a folder to save",pos=(20,30))
button.Bind(wx.EVT_BUTTON,folderChoice)

button2 = wx.Button(panel, label="Choose a folder to update",pos=(300,30))
button2.Bind(wx.EVT_BUTTON,folderChoice)

# Loop of the app
app.MainLoop()