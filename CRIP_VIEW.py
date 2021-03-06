# Import the wxPython GUI package
import wx

class MY_FRAME(wx.Frame):
  
  def __init__(self, parent, id, title):
    # Call the base class' __init__ method to create the frame
    wx.Frame.__init__(self, parent, id, title)
    
    # Associate some events with the methods of this class
    self.Bind(wx.EVT_SIZE, self.OnSize)
    self.Bind(wx.EVT_MOVE, self.OnMove)
    
    # Add a panel and some controls to display the size and position
    panel = wx.Panel(self, -1)
    position = wx.Point(100,5) # TODO: this isn't working
    size = wx.Size(100, 500)
    list1 = wx.ListBox(self, id, position, size)
    self.panel = panel
    
    # Use some sizers for layout of the widgets
    sizer = wx.FlexGridSizer(2, 2, 5, 5)
    sizer.Add(list1)
    border = wx.BoxSizer()
    border.Add(sizer, 0, wx.ALL, 15)
    panel.SetSizerAndFit(border)
    self.Fit()
  
  # This method is called by the System when the window is resized,
  # because of the association above.
  def OnSize(self, event):
    size = event.GetSize()
    
    # tell the event system to continue looking for an event handler,
    # so the default handler will get called.
    event.skip()
  
  # This method is called by the System when the window is moved,
  # because of the association above.
  def OnMove(self, event):
    pos = event.GetPosition()
    self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))

# Every wxWidgets application must have a class derived from wx.App
class MY_APP(wx.App):
  
  # wxWindows calls this method to initialize the application
  def OnInit(self):
    
    # Create an instance of our customized Frame class
    frame = MY_FRAME(None, -1, "This is a test")
    frame.Show()
    
    # Tell wxWindows that this is our main window
    self.SetTopWindow(frame)
    
    # Return a success flag
    return True

app = MY_APP(0)   # Create an instance of the application class
app.MainLoop()    # Tell it to start processing events















