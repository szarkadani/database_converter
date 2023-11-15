from gui import DatabaseConverter
import wx

if __name__ == '__main__':
    app = wx.App()
    frame = DatabaseConverter(
        None, title='Database Converter', size=(600, 400))
    frame.Show()
    app.MainLoop()
