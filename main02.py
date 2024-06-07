import wx

app = wx.App()
frame = wx.Frame(None, title="Little app")
# frame.SetBackgroundColour("#657996")
panel = wx.Panel(frame)

frame.Center()
frame.Show(True)
app.MainLoop()