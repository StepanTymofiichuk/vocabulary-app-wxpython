import wx # wxPython for GUI
import json # For handling JSON configurations
import sqlite3 # SQLite for database handling
import traceback  # Provides utilities for stack tracing of program errors.
import sys        # Provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
import winsound   # Access to the basic sound-playing for Windows platforms.

class Vocabulary:

    def __init__(self, table: str) -> None:
        self.table = table
    
    def print_vocabulary(self):
        # print passed parameters
        print(f"T: {self.table}")


    def clear_db(self):
        # Connect to db then set studied=0 for a table passsed
        db = db_name
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
        self.frame = MyFrame(None, title=app_name)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        self.frame.Maximize(True)
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
        self.table_name = wx.StaticText(panel, label=table_name)
        self.table_name.SetFont(font)
        self.table_name_entry = wx.ComboBox(panel, value="", choices=tables)
        self.table_name_entry.SetFont(font)
        # Create button
        self.btn_clear = wx.Button(panel, -1, label=clear_button_name)
        self.btn_clear.SetToolTip(wx.ToolTip(clear_btn_tooltip))
        self.btn_clear.SetFont(font)
        self.status = wx.StaticText(panel, label="")
        self.status.SetFont(font)
        # Display text label, entry field and button
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

        randId = wx.NewIdRef()
        randId1 = wx.NewIdRef()
        # Create an AcceleratorTable
        accel_tbl = wx.AcceleratorTable([
            (wx.ACCEL_CTRL,  ord('a'), randId ),
            (wx.ACCEL_CTRL,  ord('q'), randId1 )
        ])
        self.SetAcceleratorTable(accel_tbl)
        # Bind the keyboard shortcut to the button event
        self.Bind(wx.EVT_MENU, self.OnButton, id=randId)
        self.Bind(wx.EVT_MENU, self.OnExit, id=randId1)

    def OnExit(self, event):
        self.Close()

    def OnButton(self, event):
        # Handle button click event
        table_name: str = self.table_name_entry.GetStringSelection()
        if (table_name != ""):
            # Pass parameters to Vocabulary class
            v1 = Vocabulary(table_name.lower())
            v1.print_vocabulary()
            v1.clear_db()
            self.status.SetLabel(clear_success_msg)
            try:
                winsound.PlaySound("sounds/true.wav", winsound.SND_FILENAME)
            except:
                print("Sound file not found")
        else:
            self.status.SetLabel(clear_fail_msg)
            try:
                winsound.PlaySound("sounds/false.wav", winsound.SND_FILENAME)
            except:
                print("Sound file not found")
        self.btn_clear.Enable()


if __name__ == "__main__":
    try:
        with open('config.json', 'r') as  file:
            # Load configuration from JSON file
            data = json.load(file)
            app_name: str = data["localization"][0]["clear_app"]["clear_app_name"]
            db_name: str = data["db_name"]
            table_name: str = data["localization"][0]["clear_app"]["table_name"]
            clear_button_name: str = data["localization"][0]["clear_app"]["clear_button_name"]
            clear_btn_tooltip: str = data["localization"][0]["clear_app"]["clear_button_tooltip"]
            clear_success_msg: str = data["localization"][0]["clear_app"]["clear_success_msg"]
            clear_fail_msg: str = data["localization"][0]["clear_app"]["clear_fail_msg"]
            print("Success!")
        # Connect to db and view existing tables
        query = "SELECT name FROM sqlite_master WHERE type='table'"
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute(query)
        res = c.fetchall()
        conn.close()
        # Convert list of tables
        tables: list = []
        for i in res:
            tables.append(i[0])
        #print(tables)
        # Start the application
        app = ClearApp(False)
        app.MainLoop()
    except:
        print("config.json file not found, please add file to the root directory")
