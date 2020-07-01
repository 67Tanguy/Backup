#!/usr/bin/env python

import wx

class Frame(wx.Frame):
    """
    the main frame of the app
    """

    def __init__(self, *args, **kw):
        super(Frame, self).__init__(*args, **kw)
        pnl = wx.Panel(self)
        self.SetMinSize((720,480))
        self.SetMaxSize(wx.DisplaySize())

        # create a menu bar
        self.makeMenuBar()

        # Create and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to backup ! try to not screw-up your data this time !")
        

    def makeMenuBar(self):
        """
        Create a menu bar with short-cuts
        """

        # create a menu
        fileMenu = wx.Menu()
        
        # create the two sub menus with short-cut
        new = fileMenu.Append(-1, "&New backup\tCtrl-N",
                "Start to backup a new folder or file")
        fileMenu.AppendSeparator()
        seeOld = fileMenu.Append(-1, "&browse file\tCtrl-B",
                "browse file in the timeline")
        
        # label
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Add another item to the menu
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # handler of the different items 
        self.Bind(wx.EVT_MENU, self.OnNew, new)
        self.Bind(wx.EVT_MENU, self.OnSeeOld, seeOld)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    # The functions called in the handler

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnNew(self, event):
        """inform the user of his choice to backup a folder/file."""
        wx.MessageBox("you have chosen to backup a new folder")
    
    def OnSeeOld(self, event):
        """inform the user of his choice to see his backup"""
        wx.MessageBox("you have chosen to see your backup")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a python based app to help people save time while they are trying to save files and have a versioning systeme",
                      "About backup",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # Just a simple test to try this module
    app = wx.App()
    frm = Frame(None, title='Backup')
    frm.Show()
    frm.Title = "Backup"
    app.MainLoop()