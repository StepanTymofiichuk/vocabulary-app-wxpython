from subprocess import Popen
import wx
import sqlite3

python_bin = ".venv\\Scripts\\python"
db = "ItalianStudent.db"
conn = sqlite3.connect(db)
c = conn.cursor()
query = "SELECT word, translation, studied FROM italiano_parlato UNION SELECT word, translation, studied FROM frasi_italiane_parlato"
c.execute(query)
rows = c.fetchall()

class MyApp(wx.App):

    def OnInit(self):
        self.frame = MyFrame(None, title="Il Testo Del Vocabulario", size=(450,580))
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
        level1_menu = wx.Menu()
        level2_menu = wx.Menu()
        level3_menu = wx.Menu()
        exitMenuItem = fileMenu.Append(-1, "Exit", "Exit the application")
        level1_menu_item = level1_menu.Append(-1, "italiano_parlato", "test italiano parlato")
        level1_menu_item1 = level1_menu.Append(-1, "frasi_italiano_parlato", "test italiano parlato")
        level2_menu_item = level2_menu.Append(-1, "italiano_parlato", "test italiano parlato")
        level2_menu_item1 = level2_menu.Append(-1, "frasi_italiano_parlato", "test italiano parlato")
        level3_menu_item = level3_menu.Append(-1, "italiano_parlato", "test italiano parlato")
        level3_menu_item1 = level3_menu.Append(-1, "frasi_italiano_parlato", "test italiano parlato")
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(level1_menu, "&Livello 1")
        menuBar.Append(level2_menu, "&Livello 2")
        menuBar.Append(level3_menu, "&Livello 3")
        self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)
        self.Bind(wx.EVT_MENU, self.onTestLevel1, level1_menu_item)
        self.Bind(wx.EVT_MENU, self.onTestLevel1_1, level1_menu_item1)
        self.Bind(wx.EVT_MENU, self.onTestLevel2, level2_menu_item)
        self.Bind(wx.EVT_MENU, self.onTestLevel2_1, level2_menu_item1)
        self.Bind(wx.EVT_MENU, self.onTestLevel3, level3_menu_item)
        self.Bind(wx.EVT_MENU, self.onTestLevel3_1, level3_menu_item1)
        self.SetMenuBar(menuBar)

    def onTestLevel1(self, event):
        print("Test Level 1 italiano parlato")
        script_file = "level1\\test-italiano_parlato.py"
        Popen([python_bin, script_file])

    def onTestLevel1_1(self, event):
        print("Test Level 1 frasi italiano parlato")
        script_file = "level1\\test_frasi_italiane_parlato.py"
        Popen([python_bin, script_file])

    def onTestLevel2(self, event):
        print("Test Level 2 italiano parlato")
        script_file = "level2\\test-italiano_parlato.py"
        Popen([python_bin, script_file])

    def onTestLevel2_1(self, event):
        print("Test Level 2 frasi italiano parlato")
        script_file = "level2\\test_frasi_italiane_parlato.py"
        Popen([python_bin, script_file])

    def onTestLevel3(self, event):
        print("Test Level 3 italiano parlato")
        script_file = "level3\\test-italiano_parlato.py"
        Popen([python_bin, script_file])

    def onTestLevel3_1(self, event):
        print("Test Level 3 frasi italiano parlato")
        script_file = "level3\\test_frasi_italiane_parlato.py"
        Popen([python_bin, script_file])

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
        add_to_db_button = wx.Button(controls_box, -1, label="Inserire Al db", pos=(10,18))
        self.Bind(wx.EVT_BUTTON, self.AddToDbButton, id=add_to_db_button.GetId())

    def AddToDbButton(self, event):
        print("Clicked")
        script_file = "add.py"
        Popen([python_bin, script_file])

    def OnButton(self, event):
        global search_textCtrl
        global db_listControl
        value = search_textCtrl.GetValue()
        query = "SELECT * FROM italiano_parlato WHERE word LIKE '%" + value + "%' OR translation LIKE'%" + value + "%'  UNION SELECT * FROM frasi_italiane_parlato WHERE word LIKE '%" + value + "%' OR translation LIKE'%" + value + "%' "
        c.execute(query)
        rows = c.fetchall()
        db_listControl.DeleteAllItems()
        for i in rows:
            db_listControl.Append(i)

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
