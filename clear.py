import wx
import sqlite3
import traceback
import sys
import winsound

class Vocabulary:

    def __init__(self, table: str) -> None:
        self.table = table
    
    def print_vocabulary(self):
        print(f"T: {self.table}")


    def clear_db(self):
        db = "ItalianStudent.db"
        conn = sqlite3.connect(db)
        c = conn.cursor()
        try:
            delete_query = "UPDATE " + self.table + " SET studied=0"
            c.execute(delete_query)
            conn.commit()        
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        conn.close()


class ClearApp(wx.App):

    def OnInit(self):
        self.frame = MyFrame(None, title="Eliminari i progressi studiati")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MyFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        #Attributes
        self.SetBackgroundColour("WHITE")
        self.SetIcon(wx.Icon("icon.png"))

        font = wx.Font(wx.FontInfo(14).FaceName("Helvetica"))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)      
        #h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.table_name = wx.StaticText(panel, label="Nomme Della Tabela")
        self.table_name.SetFont(font)
        self.table_name_entry = wx.TextCtrl(panel)
        self.table_name_entry.SetFont(font)
        self.btn_clear = wx.Button(panel, -1, label="Azzerare")
        self.btn_clear.SetFont(font)
        self.status = wx.StaticText(panel, label="")
        self.status.SetFont(font)
        sizer.Add(0,3,0)
        sizer.Add(self.table_name,0,wx.ALIGN_LEFT,0)
        sizer.Add(0,3,0)
        sizer.Add(self.table_name_entry,0,wx.EXPAND,0)
        sizer.Add(0,3,0)
        sizer.Add(self.btn_clear,0,wx.ALIGN_LEFT,0)
        sizer.Add(0,3,0)
        sizer.Add(self.status,0,wx.EXPAND,0)
        panel.SetSizer(sizer)

        self.Bind(wx.EVT_BUTTON, self.OnButton, id=self.btn_clear.GetId())

    def OnButton(self, event):
        table_name: str = self.table_name_entry.GetValue()
        if (table_name != ""):
            v1 = Vocabulary(table_name.lower())
            v1.print_vocabulary()
            v1.clear_db()
            self.status.SetLabel("Azzerare Con Successo!")
            try:
                winsound.PlaySound("sounds/true.wav", winsound.SND_FILENAME)
            except:
                print("Sound file not found")
        else:
            self.status.SetLabel("Si prega di compilare tutti i campi!")
            try:
                winsound.PlaySound("sounds/false.wav", winsound.SND_FILENAME)
            except:
                print("Sound file not found")
        self.btn_clear.Enable()


if __name__ == "__main__":
    app = ClearApp(False)
    app.MainLoop()
