from subprocess import Popen
import wx
import sqlite3

python_bin = ".venv\\Scripts\\python"
db = "ItalianStudent.db"
conn = sqlite3.connect(db)
c = conn.cursor()
query = "SELECT word, translation, studied FROM time UNION SELECT word, translation, studied FROM calendario"
c.execute(query)
rows = c.fetchall()

class MyApp(wx.App):

    def OnInit(self):
        self.frame = MyFrame(None, title="VocabularyTest", size=(450,580))
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True 

class MyFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        self.MenuBar()
        self.Search()
        self.Database()
        self.Controls()

        #Attributes
        self.SetBackgroundColour("WHITE")
        self.SetIcon(wx.Icon("icon.png"))

    def MenuBar(self):

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitMenuItem = fileMenu.Append(-1, "Exit", "Exit the application")
        menuBar.Append(fileMenu, "&File")
        self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)
        self.SetMenuBar(menuBar)

    def onExit(self, event):
        self.Close()
    
    def Search(self):
            
        #panel1 = wx.Panel(self, size=(400,40), pos=(10,0))
        search_box = wx.StaticBox(self, label="Search Functionality", size=(390,50), pos=(10,5), style=1)
        search_text = wx.StaticText(search_box, label="Search", pos=(20,25))
        font = wx.Font(wx.FontInfo(12).FaceName("Helvetica"))
        #search_text.SetFont(font)
        global search_textCtrl
        search_textCtrl = wx.TextCtrl(search_box, value=str(len(rows)) + " words", pos=(60,18))
        search_button = wx.Button(search_box, -1, label="Go", pos=(180,18))
        refresh_button = wx.Button(search_box, label="Refresh", pos=(260,18))
        self.Bind(wx.EVT_BUTTON, self.OnButton, id=search_button.GetId())

    def Database(self):

        #panel = wx.Panel(self, size=(400,400), pos=(10,60))
        db_box = wx.StaticBox(self, label="Databae Functionality", size=(390,390), pos=(10,60))
        global db_listControl
        db_listControl = wx.ListCtrl(db_box, style=wx.LC_REPORT, pos=(20,20), size=(350,350))
        db_listControl.InsertColumn(0, "Word")
        db_listControl.InsertColumn(1, "Translation")
        db_listControl.InsertColumn(2, "Studied %")
        db_listControl.SetColumnWidth(0, 120)
        db_listControl.SetColumnWidth(1, 120)
        db_listControl.SetColumnWidth(2, 80)
        for item in rows:
            db_listControl.Append(item)

    def Controls(self):

        controls_box = wx.StaticBox(self, label="Controls", size=(390,50), pos=(10,450))
        add_to_db_button = wx.Button(controls_box, -1, label="Add To db", pos=(10,18))
        start_time_button = wx.Button(controls_box, -1, label="Time Test", pos=(85,18))
        start_calendario_button = wx.Button(controls_box, -1, label="Calendario Test", pos=(155,18))
        start_numeri_button = wx.Button(controls_box, -1, label="Numeri Test", pos=(250,18))
        self.Bind(wx.EVT_BUTTON, self.AddToDbButton, id=add_to_db_button.GetId())
        self.Bind(wx.EVT_BUTTON, self.StartTimeTestButton, id=start_time_button.GetId())
        self.Bind(wx.EVT_BUTTON, self.StartCalendarioTestButton, id=start_calendario_button.GetId())
        self.Bind(wx.EVT_BUTTON, self.StartNumeriTestButton, id=start_numeri_button.GetId())

    def AddToDbButton(self, event):
        print("Clicked")
        script_file = "add.py"
        Popen([python_bin, script_file])

    def StartTimeTestButton(self, event):
        print("Clicked")
        script_file = "test-time.py"
        Popen([python_bin, script_file])

    def StartCalendarioTestButton(self, event):
        print("Clicked")
        script_file = "test-calendario.py"
        Popen([python_bin, script_file])

    def StartNumeriTestButton(self, event):
        print("Clicked")
        script_file = "test-numeri.py"
        Popen([python_bin, script_file])

    def OnButton(self, event):
        global search_textCtrl
        global db_listControl
        value = search_textCtrl.GetValue()
        query = "SELECT * FROM time WHERE word LIKE '%" + value + "%' OR translation LIKE'%" + value + "%'  UNION SELECT * FROM calendario WHERE word LIKE '%" + value + "%' OR translation LIKE'%" + value + "%' "
        c.execute(query)
        rows = c.fetchall()
        db_listControl.DeleteAllItems()
        for i in rows:
            db_listControl.Append(i)

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
