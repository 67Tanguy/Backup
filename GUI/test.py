import wx
import wx.grid
import Frame

class GridFrame(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Create a wxGrid object
        grid = wx.grid.Grid(self, -1)

        # Create a grid 
        grid.CreateGrid(3, 2)

        grid.SetRowSize(0, 100)
        grid.SetColSize(0, 100)

        self.Show()


if __name__ == '__main__':

    app = wx.App(0)
    frm = Frame.Frame(None, title='Backup',size=(1080,720))
    panel = wx.Panel(frm)
    panel.SetSize(frm.GetSize())
    gframe=GridFrame(panel)
    frm.Show()
    frm.Title = "Backup"
    app.MainLoop()