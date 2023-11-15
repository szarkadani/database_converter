import wx
import wx.grid
from db_connector import DatabaseConnectionManager
from csv_exporter import export_table_to_csv


class DatabaseConverter(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(DatabaseConverter, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        panel = wx.Panel(self)

        with DatabaseConnectionManager() as cursor:
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]

            self.grid = wx.grid.Grid(panel, -1)
            self.grid.CreateGrid(len(tables), 2)

            self.grid.SetColLabelValue(0, "Export")
            self.grid.SetColLabelValue(1, "Table Name")

            self.grid.SetColFormatBool(0)

            for i, table_name in enumerate(tables):
                self.grid.SetCellValue(i, 1, table_name)

            save_btn = wx.Button(panel, label='Save')
            save_btn.Bind(wx.EVT_BUTTON, self.on_save)

            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self.grid, 1, flag=wx.EXPAND)
            sizer.Add(save_btn, 0, flag=wx.EXPAND)

            panel.SetSizer(sizer)

    def on_save(self, event):
        with DatabaseConnectionManager() as cursor:
            for i in range(self.grid.GetNumberRows()):
                if self.grid.GetCellValue(i, 0) == '1':
                    table_name = self.grid.GetCellValue(i, 1)
                    export_table_to_csv(cursor, table_name)

        wx.MessageBox('Tables exported successfully!',
                      'Info', wx.OK | wx.ICON_INFORMATION)
