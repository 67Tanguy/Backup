#!/usr/bin/env python

import wx
import gui.Frame as Frame

# create the app
app = wx.App()

#create the frame with min and max size
frm = Frame.Frame(None, title='Backup',size=(1080,720))
frm.Title = "Backup"
frm.mypanel()
frm.Show()

# Loop of the app
app.MainLoop()