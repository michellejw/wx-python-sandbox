"""
Hello, world!

More or less directly following this example: https://wxpython.org/pages/overview/#hello-world
"""

import wx


class HelloFrame(wx.Frame):
    """
    A Frame that says "Hello, world!"
    """

    def __init__(self, *args, **kw):
        # Ensure that the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        # Create a panel in the frame
        pnl = wx.Panel(self)

        # Add some text with a larger bold font on it
        st = wx.StaticText(pnl, label='Hello, world!')
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # Create a sizer to manage the layout of the child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        pnl.SetSizer(sizer)

        # Create a menu bar
        self.make_menu_bar()

        # Add a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython! Love, Michelle")

    def make_menu_bar(self):
        """
        Make the menu bar. It can have multiple menus and each menu has menu items. This method builds a set of menus
        and binds handlers to be called when the menu item is selected.

        """

        # Make a file menu with Hello and Exit items
        file_menu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        hello_item = file_menu.Append(-1, "&Hello...\tCtrl-H",
                                      "Help string shown in status bar for this menu item")
        file_menu.AppendSeparator()

        # When using a stock ID we don't need to specify the menu item's label
        exit_item = file_menu.Append(wx.ID_EXIT)

        # Next, a help menu for the about item
        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT)

        # Make the menu bar and add menus. The '&' sets up the mnemonic for the menu item. On some
        # systems this will show that first letter as underlined and allows for keyboard shortcuts.
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(help_menu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menu_bar)

        # Finally, use EVT_MENU to link a handler function with each menu item. That means that when
        # the menu item is selected, the associated handler will be called
        self.Bind(wx.EVT_MENU, self.on_hello, hello_item)
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)
        self.Bind(wx.EVT_MENU, self.on_about, about_item)

    def on_exit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    @staticmethod
    def on_hello(event):
        """Say hello to the user"""
        wx.MessageBox("Hello again from wxPython and Michelle!")

    @staticmethod
    def on_about(event):
        """Display an about dialog"""
        wx.MessageBox("This is a wxPython Hello World Example",
                      "About the Hello World app",
                      wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':
    # When this module is run (not imported), create the app, the frame, show it,
    # and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title="Hello World!! <3")
    frm.Show()
    app.MainLoop()
