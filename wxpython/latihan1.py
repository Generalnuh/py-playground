import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))
        
        panel = wx.Panel(self)
        self.text_ctrl = wx.TextCtrl(panel, pos=(10, 10))
        btn = wx.Button(panel, label="Klik Saya!", pos=(10, 50))
        btn.Bind(wx.EVT_BUTTON, self.on_button_click)
        
        self.Show(True)
        
    def on_button_click(self, event):
        self.text_ctrl.SetValue("Tombol telah diklik!")

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "Contoh Aplikasi wxPython")
    app.MainLoop()
