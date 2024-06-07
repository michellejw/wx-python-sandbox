import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        pnl = wx.Panel(self)
        st = wx.StaticText(pnl, label="Hello World!", pos=(25, 25))

        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        self.make_menu_bar()
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")

    def make_menu_bar(self):
        file_menu = wx.Menu()
        hello_item = file_menu.Append(-1, "&Hello...\tCtrl-H",
                                      "Help string shown in the status bar for this menu item.")
        file_menu.AppendSeparator()
        exit_item = file_menu.Append(wx.ID_EXIT)

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, self.on_hello, hello_item)
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)

    @staticmethod
    def on_exit(_):
        exit()

    @staticmethod
    def on_hello(_):
        wx.MessageBox("Hello again from wxPython!")


if __name__ == '__main__':
    app = wx.App(False)
    frm = MyFrame(None, title="Hello World", size=(400, 300))
    frm.Show()
    app.MainLoop()
