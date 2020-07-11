#!/usr/bin/env python

import wx
from pathlib import Path
import os
import sys 
fullPath = str(Path(__file__).absolute().parent.parent)
sys.path.append(fullPath + "/files")
import CpFile as cp


class Frame(wx.Frame):
    """
    the main frame of the app
    """

    def __init__(self, *args, **kw):
        super(Frame, self).__init__(*args, **kw)
        self.SetMinSize((720,480))
        self.SetMaxSize(wx.DisplaySize())
        self.Centre()
        # create a menu bar
        self.makeMenuBar()

        # Create and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to backup ! try to not screw-up your data this time !")
        self.src = ""
        self.dst = ""
        self.srcBoxListe = wx.BoxSizer(wx.VERTICAL)

        


        
        
        

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

    def folderSrc(self, event):
        selector = wx.DirSelector("choose a folder")
        if (selector):
            #self.srcFinal.Hide()
            self.src = selector
            print(self.src)
            #self.srcFolderDisplay()
        
        return selector.strip()
    
    def folderDst(self, event):
        selector = wx.DirSelector("choose a folder")
        if (selector):
            self.dst = selector
            print(self.dst)  
        return selector.strip()
    
    
            

    def mypanel(self):

        panel = wx.Panel(self)
        panel.Fit()

        container = wx.BoxSizer(wx.VERTICAL)

        intro = wx.StaticText(panel,label=" Welcome to Backup, the app that allow safe backup easly !")
        fullPath = str(Path(__file__).absolute().parent.parent)
        
        srcBox = wx.BoxSizer(wx.VERTICAL)
        dstBox = wx.BoxSizer(wx.VERTICAL)
       
        srcImg = wx.Image(fullPath+"/assets/png/add.png")
        srcBmp=srcImg.Scale(int(srcImg.GetWidth()/4),int(srcImg.GetHeight()/4)).ConvertToBitmap()
        self.srcFinal = wx.StaticBitmap(panel, -1, srcBmp)
    

        src = wx.Button(panel, label= "choose the folder to save")
        src.Bind(wx.EVT_BUTTON,self.folderSrc)

        dstImg = wx.Image(fullPath+"/assets/png/add.png")
        dstBmp=dstImg.Scale(int(dstImg.GetWidth()/4),int(dstImg.GetHeight()/4)).ConvertToBitmap()
        self.dstFinal = wx.StaticBitmap(panel, -1, dstBmp)

        dst = wx.Button(panel, label= "Choose the location to save the folder")
        dst.Bind(wx.EVT_BUTTON,self.folderDst)
        
        
        arrowImg = wx.Image(fullPath+"/assets/png/arrow.png")
        arrowBmp=arrowImg.Scale(int(arrowImg.GetWidth()/4),int(arrowImg.GetHeight()/4)).ConvertToBitmap()
        arrow = wx.StaticBitmap(panel, -1, arrowBmp)


        submit = wx.Button(panel, label="Submit")
        submit.Bind(wx.EVT_BUTTON,self.OnSubmit)

        box = wx.BoxSizer(wx.HORIZONTAL)

        box.AddStretchSpacer()
        box.Add(srcBox, flag=wx.ALIGN_CENTER)
        box.AddSpacer(20)
        box.Add(arrow, flag=wx.ALIGN_CENTER)
        box.AddSpacer(20)
        box.Add(dstBox, flag=wx.ALIGN_CENTER)
        box.AddStretchSpacer()

        container.AddStretchSpacer()
        container.Add(intro,flag=wx.ALIGN_CENTER)
        container.AddSpacer(50)
        container.Add(box,flag=wx.ALIGN_CENTER)
        container.AddSpacer(50)
        container.Add(submit,flag=wx.ALIGN_CENTER)
        container.AddStretchSpacer()

        srcBox.AddStretchSpacer()
        srcBox.Add(self.srcFinal, flag=wx.ALIGN_CENTER)
        srcBox.Add(self.srcBoxListe, flag=wx.ALIGN_CENTER)
        srcBox.Add(src, flag=wx.ALIGN_CENTER)
        srcBox.AddStretchSpacer()

        dstBox.AddStretchSpacer()
        dstBox.Add(self.dstFinal, flag=wx.ALIGN_CENTER)
        dstBox.Add(dst, flag=wx.ALIGN_CENTER)
        dstBox.AddStretchSpacer()

        panel.SetSizer(container)
        panel.Layout()



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
    
    def OnSubmit(self, event):
        """Do a copy of the src to dst"""
        if self.dst and self.src :
            if self.src in self.dst :
                wx.MessageBox("You can not choose this destination because it's in the source folder.","Information", wx.OK  | wx.ICON_INFORMATION)
            else :
                new = self.dst+"/"+os.path.basename(self.src)
                file=cp.CpFile(self.src,new)
                str_message = "You have choosen to copy "+ os.path.basename(self.src)+" to the folder "+ os.path.basename(self.dst)
                res=""
        
                message = wx.MessageBox(str_message,"copy", wx.OK | wx.CANCEL | wx.ICON_INFORMATION)
                if message==wx.OK : 
                    res=file.copy()
                if res:
                    if self.dst!=str(Path(self.src).absolute().parent):
                        res_err=file.fail()
                        if res_err:
                            wx.MessageBox(str(res_err),"ERROR", wx.OK | wx.ICON_ERROR)
                    wx.MessageBox(str(res),"ERROR", wx.OK | wx.ICON_ERROR)
                else :
                    wx.MessageBox("The copy has been made !","Copy", wx.OK  | wx.ICON_INFORMATION)
        else :
            wx.MessageBox("You have to choose the source folder or the destination","Information", wx.OK  | wx.ICON_INFORMATION)

            


if __name__ == '__main__':
    # Just a simple test to try this module
    app = wx.App()
    frm = Frame(None, title='Backup')
    frm.Show()
    frm.Title = "Backup"
    frm.mypanel()
    app.MainLoop()