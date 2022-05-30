import wx


class Persona(wx.App):

    def __init__(self, redirect=False, filename=None, useBestVisual=False, clearSigInt=True):
        super().__init__(redirect=False, filename=None, useBestVisual=False, clearSigInt=True)
        self.frame = FrmPersona(None)
        self.frame.Show()


class FrmPersona(wx.Frame):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.SetTitle("Tutoria de wxPython")

        self.mypanel = wx.Panel(self, wx.ID_ANY)

        self.lbNom = wx.StaticText(self.mypanel, wx.ID_ANY, label="Nombre:")
        self.txtNom = wx.TextCtrl(self.mypanel, wx.ID_ANY, '')

        self.btnAceptar = wx.Button(self.mypanel, wx.ID_ANY, label="Aceptar")
        self.Bind(wx.EVT_BUTTON, self.clik, self.btnAceptar)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.lbNom, 0, wx.ALL, 5)
        hbox.Add(self.txtNom, 1, wx.ALL, 5)
        hbox.Add(self.btnAceptar, 0, wx.ALL, 5)
        self.mypanel.SetSizer(hbox)

    def clik(self, event):
        if self.txtNom.IsEmpty() is not True:
            content = self.txtNom.GetValue()
            print(content)
            self.txtNom.Clear()
        wx.MessageBox("Escriba un nombre", "Mensaje Informativo")


if __name__ == "__main__":
    app = Persona(False)
    app.MainLoop()
