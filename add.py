import wx
import sqlite3

# db = "SpanishStudent.db"
# conn = sqlite3.connect(db)
# c = conn.cursor()
# query = "SELECT * FROM ropa"
# c.execute(query)
# rows = c.fetchall()


class Add(wx.App):

    def OnInit(self):
        self.frame = MyFrame(None, title="Add word")
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
        self.table_name = wx.StaticText(panel, label="Table Name")
        self.table_name.SetFont(font)
        self.table_name_entry = wx.TextCtrl(panel)
        self.table_name_entry.SetFont(font)
        self.word = wx.StaticText(panel, label="Word")
        self.word.SetFont(font)
        self.word_entry = wx.TextCtrl(panel)
        self.word_entry.SetFont(font)
        self.translation = wx.StaticText(panel, label="Translation")
        self.translation.SetFont(font)
        self.translation_entry = wx.TextCtrl(panel)
        self.translation_entry.SetFont(font)
        self.btn_add = wx.Button(panel, -1, label="Add")
        self.btn_add.SetFont(font)
        sizer.Add(self.table_name,0,wx.ALIGN_LEFT,0)
        sizer.Add(self.table_name_entry,0,wx.EXPAND,0)
        sizer.Add(self.word,0,wx.ALIGN_LEFT,0)
        sizer.Add(self.word_entry,0,wx.EXPAND,0)
        sizer.Add(self.translation,0,wx.ALIGN_LEFT,0)
        sizer.Add(self.translation_entry,0,wx.EXPAND,0)
        sizer.Add(self.btn_add,0,wx.ALIGN_LEFT,0)
        panel.SetSizer(sizer)

        self.Bind(wx.EVT_BUTTON, self.OnButton, id=self.btn_add.GetId())

    def OnButton(self, event):
        table_name_add = self.table_name_entry.GetValue()
        word_add = self.word_entry.GetValue()
        translation_add  = self.translation_entry.GetValue()
        print(word_add)
        print(translation_add)
        table_name = table_name_add
        db = "ItalianStudent.db"
        conn = sqlite3.connect(db)
        c = conn.cursor()
        create_table_query = "CREATE TABLE IF NOT EXISTS " + table_name + " (word TEXT, translation TEXT, studied INTEGER)"
        c.execute(create_table_query)
        insert_query = "INSERT INTO " + table_name + " VALUES ('%s', '%s', '%s')" % (word_add, translation_add, 0)
        c.execute(insert_query)
        conn.commit()
        conn.close()
        self.word_entry.Clear()
        self.translation_entry.Clear()
        print("OK")

if __name__ == "__main__":
    app = Add(False)
    app.MainLoop()
