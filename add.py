import wx # wxPython for GUI
import json # For handling JSON configurations
import sqlite3 # SQLite for database handling
import traceback  # Provides utilities for stack tracing of program errors.
import sys        # Provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
import winsound   # Access to the basic sound-playing for Windows platforms.

class Vocabulary:

    def __init__(self, table: str, word: str, translation: str) -> None:
        self.table = table
        self.word = word
        self.translation = translation
    
    def print_vocabulary(self):
        # Print parameters passed
        print(f"T: {self.table}, W: {self.word}, T: {self.translation}")


    def add_to_db(self):
        # Insert passed parameters to db
        db = db_name
        conn = sqlite3.connect(db)
        c = conn.cursor()
        try:
            create_table_query = "CREATE TABLE IF NOT EXISTS " + self.table + " (word TEXT, translation TEXT, studied INTEGER)"
            c.execute(create_table_query)
            insert_query = "INSERT INTO " + self.table + " VALUES ('%s', '%s', '%s')" % (self.word, self.translation, 0)
            c.execute(insert_query)
            conn.commit()        
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        conn.close()


class Add(wx.App):

    def OnInit(self):
        self.frame = MyFrame(None, title=app_name)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MyFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        #Set up attributes
        self.SetBackgroundColour("WHITE")
        self.SetIcon(wx.Icon("icon.png"))

        font = wx.Font(wx.FontInfo(14).FaceName("Helvetica"))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)   
        # Create text label and entry field
        self.table_name = wx.StaticText(panel, label=insert_table_name)
        self.table_name.SetFont(font)
        self.table_name_entry = wx.ComboBox(panel, value="", choices=[table1, table2])
        self.table_name_entry.SetFont(font)
        # Create text label and entry field
        self.word = wx.StaticText(panel, label=insert_word_name)
        self.word.SetFont(font)
        self.word_entry = wx.TextCtrl(panel)
        self.word_entry.SetFont(font)
        # Create text label and entry field
        self.translation = wx.StaticText(panel, label=insert_translation_name)
        self.translation.SetFont(font)
        self.translation_entry = wx.TextCtrl(panel)
        self.translation_entry.SetFont(font)
        # Create text label and entry field
        self.btn_add = wx.Button(panel, -1, label=insert_button_name)
        self.btn_add.SetFont(font)
        self.status = wx.StaticText(panel, label="")
        self.status.SetFont(font)
        # Display text labels and entry fields
        sizer.Add(0,3,0)
        sizer.Add(self.table_name,0,wx.ALIGN_LEFT,0)
        sizer.Add(0,3,0)
        sizer.Add(self.table_name_entry,0,wx.EXPAND,0)
        sizer.Add(0,3,0)
        sizer.Add(self.word,0,wx.ALIGN_LEFT,0)
        sizer.Add(0,3,0)
        sizer.Add(self.word_entry,0,wx.EXPAND,0)
        sizer.Add(0,3,0)
        sizer.Add(self.translation,0,wx.ALIGN_LEFT,0)
        sizer.Add(0,3,0)
        sizer.Add(self.translation_entry,0,wx.EXPAND,0)
        sizer.Add(0,3,0)
        sizer.Add(self.btn_add,0,wx.ALIGN_LEFT,0)
        sizer.Add(0,3,0)
        sizer.Add(self.status,0,wx.ALIGN_CENTER,0)
        panel.SetSizer(sizer)

        self.Bind(wx.EVT_BUTTON, self.OnButton, id=self.btn_add.GetId())

    def OnButton(self, event):
        # Handle button click event
        table_name_add: str = self.table_name_entry.GetStringSelection()
        #print(table_name_add)
        self.btn_add.Disable()
        word_add: str = self.word_entry.GetValue()
        translation_add: str  = self.translation_entry.GetValue()
        if (table_name_add != "" and word_add != "" and translation_add != ""):
            # Pass parameters to Vocabulary class
            v1 = Vocabulary(table_name_add.lower(), word_add, translation_add)
            v1.print_vocabulary()
            v1.add_to_db()
            self.word_entry.Clear()
            self.translation_entry.Clear()
            self.status.SetLabel(insert_success_msg)
            try:
                winsound.PlaySound("sounds/true.wav", winsound.SND_FILENAME)
            except:
                print("Sound file not found")
        else:
            self.status.SetLabel(insert_fail_msg)
            try:
                winsound.PlaySound("sounds/false.wav", winsound.SND_FILENAME)
            except:
                print("Sound file not found")
        self.btn_add.Enable()


if __name__ == "__main__":
    try:
        with open('config.json', 'r') as file:
            # Load configuration from JSON file
            data = json.load(file)
            app_name: str = data["localization"][0]["insert_app"]["insert_app_name"]
            db_name: str = data["db_name"]
            insert_table_name: str = data["localization"][0]["insert_app"]["insert_table_name"]
            insert_word_name: str = data["localization"][0]["insert_app"]["insert_word_name"]
            insert_translation_name: str =data["localization"][0]["insert_app"]["insert_translation_name"]
            insert_button_name: str = data["localization"][0]["insert_app"]["insert_button_name"]
            insert_success_msg: str = data["localization"][0]["insert_app"]["insert_success_msg"]
            insertt_fail_msg: str = data["localization"][0]["insert_app"]["insert_fail_msg"]
            table1: str = data["table1_name"]
            table2: str = data["table2_name"]
            print("Success!")

        # Start the application
        app = Add(False)
        app.MainLoop()
    except:
        print("config.json file not found, please add the file to root directory")
