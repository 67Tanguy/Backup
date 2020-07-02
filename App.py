#!/usr/bin/env python

import wx
import wx.svg
import gui.Frame as Frame


def size_change(event):
    width,height = event.GetSize()
    print ("Width =",width,"Height =",height)

# create the app
app = wx.App()

#create the frame with min and max size
frm = Frame.Frame(None, title='Backup',size=(1080,720))
frm.Title = "Backup"
frm.mypanel()
frm.Show()

# Loop of the app
app.MainLoop()