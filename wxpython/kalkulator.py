import wx

class Calculator(wx.Frame):
    def __init__(self, parent, title):
        super(Calculator, self).__init__(parent, title=title, size=(300, 250))

        # Membuat panel utama
        self.panel = wx.Panel(self)
        
        # Membuat box sizer vertikal untuk panel
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Menambahkan text control untuk menampilkan hasil
        self.display = wx.TextCtrl(self.panel, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        
        # Menambahkan tombol-tombol kalkulator
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for label in buttons:
            if label == '=':
                btn = wx.Button(self.panel, label=label, size=(70, 50))
                btn.Bind(wx.EVT_BUTTON, self.on_result)
            elif label == 'C':
                btn = wx.Button(self.panel, label=label, size=(70, 50))
                btn.Bind(wx.EVT_BUTTON, self.on_clear)
            else:
                btn = wx.Button(self.panel, label=label, size=(70, 50))
                btn.Bind(wx.EVT_BUTTON, self.on_append)
            vbox.Add(btn, flag=wx.EXPAND)

        self.panel.SetSizer(vbox)

        self.Centre()
        self.Show()

    def on_append(self, event):
        label = event.GetEventObject().GetLabel()
        self.display.AppendText(label)

    def on_clear(self, event):
        self.display.Clear()

    def on_result(self, event):
        try:
            result = eval(self.display.GetValue())
            self.display.SetValue(str(result))
        except:
            wx.MessageBox('Invalid Input!', 'Error', wx.OK | wx.ICON_ERROR)

if __name__ == '__main__':
    app = wx.App()
    Calculator(None, title='Calculator')
    app.MainLoop()
