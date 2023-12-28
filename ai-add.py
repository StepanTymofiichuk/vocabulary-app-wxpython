import wx
import sqlite3
import traceback
import sys

class Vocabulary:

    def __init__(self, table: str, word: str, translation: str) -> None:
        self.table = table.lower()
        self.word = word
        self.translation = translation
    
    def print_vocabulary(self):
        print(f"Table: {self.table}, Word: {self.word}, Translation: {self.translation}")

    def create_table(self, conn):
        create_table_query = f"CREATE TABLE IF NOT EXISTS {self.table} (word TEXT, translation TEXT, studied INTEGER)"
        conn.execute(create_table_query)

    def insert_data(self, conn):
        insert_query = f"INSERT INTO {self.table} VALUES (?, ?, ?)"
        conn.execute(insert_query, (self.word, self.translation, 0))

    def add_to_db(self):
        db = "ItalianStudent.db"
        try:
            with sqlite3.connect(db) as conn:
                self.create_table(conn)
                self.insert_data(conn)
        except sqlite3.Error as e:
            print(f'SQLite error: {str(e)}')
            print(f'Exception class: {e.__class__.__name__}')
            print('SQLite traceback:')
            traceback.print_exc()

class Add(wx.App):

    def OnInit(self):
        self.frame = MyFrame(None, title="Add word")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MyFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        self.SetBackgroundColour("WHITE")
        self.SetIcon(wx.Icon("icon.png"))

        font = wx.Font(wx.FontInfo(14).FaceName("Helvetica"))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        
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

        self.status = wx.StaticText(panel, label="")
        self.status.SetFont(font)

        sizer.Add(self.table_name, 0, wx.ALIGN_LEFT, 0)
        sizer.Add(self.table_name_entry, 0, wx.EXPAND, 0)
        sizer.Add(self.word, 0, wx.ALIGN_LEFT, 0)
        sizer.Add(self.word_entry, 0, wx.EXPAND, 0)
        sizer.Add(self.translation, 0, wx.ALIGN_LEFT, 0)
        sizer.Add(self.translation_entry, 0, wx.EXPAND, 0)
        sizer.Add(self.btn_add, 0, wx.ALIGN_LEFT, 0)
        sizer.Add(self.status, 0, wx.ALIGN_CENTER, 0)
        
        panel.SetSizer(sizer)

        self.Bind(wx.EVT_BUTTON, self.OnButton, id=self.btn_add.GetId())

    def OnButton(self, event):
        table_name_add = self.table_name_entry.GetValue()
        word_add = self.word_entry.GetValue()
        translation_add = self.translation_entry.GetValue()

        if table_name_add and word_add and translation_add:
            try:
                vocabulary = Vocabulary(table_name_add, word_add, translation_add)
                vocabulary.print_vocabulary()
                vocabulary.add_to_db()
                self.word_entry.Clear()
                self.translation_entry.Clear()
                self.status.SetLabel("Successfully added!")
            except Exception as e:
                self.status.SetLabel(f"Error: {str(e)}")
        else:
            self.status.SetLabel("Please fill in all fields")

if __name__ == "__main__":
    app = Add(False)
    app.MainLoop()