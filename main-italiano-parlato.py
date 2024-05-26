from subprocess import Popen
import wx
import sqlite3
import json

python_bin = ".venv\\Scripts\\python"

class MyApp(wx.App):

    def OnInit(self):
        self.frame = MyFrame(None, title=app_name, size=(450,580))
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True 

class MyFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        self.MenuBar()
        
        self.Search()
        self.Stats()
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
        level1_menu_item = level1_menu.Append(-1, menu_item1_name, "test italiano parlato")
        level1_menu_item1 = level1_menu.Append(-1, menu_item2_name, "test italiano parlato")
        level2_menu_item = level2_menu.Append(-1, menu_item1_name, "test italiano parlato")
        level2_menu_item1 = level2_menu.Append(-1, menu_item2_name, "test italiano parlato")
        level3_menu_item = level3_menu.Append(-1, menu_item1_name, "test italiano parlato")
        level3_menu_item1 = level3_menu.Append(-1, menu_item2_name, "test italiano parlato")
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(level1_menu, menu1_name)
        menuBar.Append(level2_menu, menu2_name)
        menuBar.Append(level3_menu, menu3_name)
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
        script_file = "level1\\" + test_words_filename
        Popen([python_bin, script_file])

    def onTestLevel1_1(self, event):
        print("Test Level 1 frasi italiano parlato")
        script_file = "level1\\" + test_phrases_filename
        Popen([python_bin, script_file])

    def onTestLevel2(self, event):
        print("Test Level 2 italiano parlato")
        script_file = "level2\\" + test_words_filename
        Popen([python_bin, script_file])

    def onTestLevel2_1(self, event):
        print("Test Level 2 frasi italiano parlato")
        script_file = "level2\\" + test_phrases_filename
        Popen([python_bin, script_file])

    def onTestLevel3(self, event):
        print("Test Level 3 italiano parlato")
        script_file = "level3\\" + test_words_filename
        Popen([python_bin, script_file])

    def onTestLevel3_1(self, event):
        print("Test Level 3 frasi italiano parlato")
        script_file = "level3\\" + test_phrases_filename
        Popen([python_bin, script_file])

    def onExit(self, event):
        self.Close()
    
    def Search(self):
            
        #panel1 = wx.Panel(self, size=(400,40), pos=(10,0))
        search_box = wx.Panel(self, size=(390,50), pos=(10,0), style=1)
        search_text = wx.StaticText(search_box, label=search_name, pos=(16,25))
        font = wx.Font(wx.FontInfo(12).FaceName("Helvetica"))
        #search_text.SetFont(font)
        global search_textCtrl
        search_textCtrl = wx.TextCtrl(search_box, value=str(len(rows)) + " "+ search_placeholder, pos=(60,18))
        search_button = wx.Button(search_box, -1, label=search_btn_name, pos=(180,18))
        refresh_button = wx.Button(search_box, label=refresh_btn_name, pos=(260,18))
        self.Bind(wx.EVT_BUTTON, self.OnButton, id=search_button.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnRefreshButton, id=refresh_button.GetId())

    def Stats(self):
        level1_query = "SELECT COUNT(word) FROM '%s' WHERE studied<20" % table1
        level2_query = "SELECT COUNT(word) FROM '%s' WHERE studied BETWEEN 20 AND 40" % table1
        level3_query = "SELECT COUNT(word) FROM '%s' WHERE studied BETWEEN 60 AND 80" %table1
        level1_fr_query = "SELECT COUNT(word) FROM '%s' WHERE studied<20" % table2
        level2_fr_query = "SELECT COUNT(word) FROM '%s' WHERE studied BETWEEN 20 AND 40" % table2
        level3_fr_query = "SELECT COUNT(word) FROM '%s' WHERE studied BETWEEN 60 AND 80" % table2
        c.execute(level1_query)
        c1 = conn.cursor()
        c2 = conn.cursor()
        c1.execute(level2_query)
        c2.execute(level3_query)
        c1_fr = conn.cursor()
        c2_fr = conn.cursor()
        c3_fr = conn.cursor()
        c1_fr.execute(level1_fr_query)
        c2_fr.execute(level2_fr_query)
        c3_fr.execute(level3_fr_query)
        lvl1_result = c.fetchone()
        lvl2_result = c1.fetchone()
        lvl3_result = c2.fetchone()
        lvl1_fr_result = c1_fr.fetchone()
        lvl2_fr_result = c2_fr.fetchone()
        lvl3_fr_result = c3_fr.fetchone()
        # print(lvl1_result)
        # print(lvl2_result)
        # print(lvl3_result)
        # print(lvl1_fr_result)
        # print(lvl2_fr_result)
        # print(lvl3_fr_result)
        stats_box = wx.StaticBox(self, size=(390,76), pos=(10,50))
        box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        title = wx.StaticText(stats_box, label=stats_box_name1, pos=(15,10))
        title_words_left = wx.StaticText(stats_box, label=stats_box_items_name, pos=(160,28))
        title1 = wx.StaticText(stats_box, label=stats_box_name2, pos=(265,10))
        font = wx.Font(wx.FontInfo(16).FaceName("Helvetica"))
        self.level1_words = wx.StaticText(stats_box, label=str(lvl1_result[0]), pos=(20, 26))
        level1_title = wx.StaticText(stats_box, label="Lvl 1", pos=(18, 50))
        self.level1_words.SetFont(font)
        self.level2_words = wx.StaticText(stats_box, label=str(lvl2_result[0]), pos=(50, 26))
        level2_title = wx.StaticText(stats_box, label="Lvl 2", pos=(48, 50))
        self.level2_words.SetFont(font)
        self.level3_words = wx.StaticText(stats_box, label=str(lvl3_result[0]), pos=(90, 26))
        level3_title = wx.StaticText(stats_box, label="Lvl 3", pos=(88, 50))
        self.level3_words.SetFont(font)
        self.level1_fr_words = wx.StaticText(stats_box, label=str(lvl1_fr_result[0]), pos=(275, 26))
        level1_fr_title = wx.StaticText(stats_box, label="Lvl 1", pos=(273, 50))
        self.level1_fr_words.SetFont(font)
        self.level2_fr_words = wx.StaticText(stats_box, label=str(lvl2_fr_result[0]), pos=(305, 26))
        level2_fr_title = wx.StaticText(stats_box, label="Lvl 2", pos=(303, 50))
        self.level2_fr_words.SetFont(font)
        self.level3_fr_words = wx.StaticText(stats_box, label=str(lvl3_fr_result[0]), pos=(345, 26))
        level3_fr_title = wx.StaticText(stats_box, label="Lvl 3", pos=(343, 50))
        self.level3_fr_words.SetFont(font)

    def Database(self):

        #panel = wx.Panel(self, size=(400,400), pos=(10,60))
        db_box = wx.Panel(self, size=(390,340), pos=(10,123))
        global db_listControl
        db_listControl = wx.ListCtrl(db_box, style=wx.LC_REPORT, pos=(20,20), size=(350,305))
        db_listControl.InsertColumn(0, db_column1_name)
        db_listControl.InsertColumn(1, db_column2_name)
        db_listControl.InsertColumn(2, db_column3_name)
        db_listControl.SetColumnWidth(0, 120)
        db_listControl.SetColumnWidth(1, 120)
        db_listControl.SetColumnWidth(2, 80)
        for item in rows:
            db_listControl.Append(item)

    def Controls(self):

        controls_box = wx.Panel(self, size=(390,50), pos=(10,450))
        add_to_db_button = wx.Button(controls_box, -1, label=insert_button_name, pos=(10,18))
        clear_from_db_button = wx.Button(controls_box, -1, label=clear_button_name, pos=(103,18))
        self.Bind(wx.EVT_BUTTON, self.AddToDbButton, id=add_to_db_button.GetId())
        self.Bind(wx.EVT_BUTTON, self.ClearDbButton, id=clear_from_db_button.GetId())

    def AddToDbButton(self, event):
        #print("Clicked")
        script_file = insert_vocab_filename
        Popen([python_bin, script_file])

    def ClearDbButton(self, event):
        #print("Clicked")
        script_file = clear_vocab_filename
        Popen([python_bin, script_file])

    def OnButton(self, event):
        global search_textCtrl
        global db_listControl
        value = search_textCtrl.GetValue()
        query = "SELECT * FROM "+ table1 +" WHERE word LIKE '%" + value + "%' OR translation LIKE'%" + value + "%'  UNION SELECT * FROM "+ table2 +" WHERE word LIKE '%" + value + "%' OR translation LIKE'%" + value + "%' "
        c.execute(query)
        rows = c.fetchall()
        db_listControl.DeleteAllItems()
        for i in rows:
            db_listControl.Append(i)

    def OnRefreshButton(self, event):
        print("Clicked")
        level1_query = "SELECT COUNT(word) FROM '%s' WHERE studied<20" % table1
        level2_query = "SELECT COUNT(word) FROM '%s' WHERE studied BETWEEN 20 AND 40" % table1
        level3_query = "SELECT COUNT(word) FROM '%s' WHERE studied BETWEEN 60 AND 80" %table1
        level1_fr_query = "SELECT COUNT(word) FROM '%s' WHERE studied<20" % table2
        level2_fr_query = "SELECT COUNT(word) FROM '%s' WHERE studied BETWEEN 20 AND 40" % table2
        level3_fr_query = "SELECT COUNT(word) FROM '%s' WHERE studied BETWEEN 60 AND 80" % table2
        c.execute(level1_query)
        c1 = conn.cursor()
        c2 = conn.cursor()
        c1.execute(level2_query)
        c2.execute(level3_query)
        c1_fr = conn.cursor()
        c2_fr = conn.cursor()
        c3_fr = conn.cursor()
        c1_fr.execute(level1_fr_query)
        c2_fr.execute(level2_fr_query)
        c3_fr.execute(level3_fr_query)
        lvl1_result = c.fetchone()
        lvl2_result = c1.fetchone()
        lvl3_result = c2.fetchone()
        lvl1_fr_result = c1_fr.fetchone()
        lvl2_fr_result = c2_fr.fetchone()
        lvl3_fr_result = c3_fr.fetchone()
        self.level1_words.SetLabel(str(lvl1_result[0]))
        self.level2_words.SetLabel(str(lvl2_result[0]))
        self.level3_words.SetLabel(str(lvl3_result[0]))
        self.level1_fr_words.SetLabel(str(lvl1_fr_result[0]))
        self.level2_fr_words.SetLabel(str(lvl2_fr_result[0]))
        self.level3_fr_words.SetLabel(str(lvl3_fr_result[0]))


if __name__ == "__main__":
    try:
        with open('config.json', 'r') as file:
            data = json.load(file)
            db = data["db_name"]
            table1: str = data["table1_name"]
            table2: str = data["table2_name"]
            app_name: str = data["localization"][0]["app_name"]
            menu1_name: str = data["localization"][0]["menu1"]
            menu2_name: str = data["localization"][0]["menu2"]
            menu3_name: str = data["localization"][0]["menu3"]
            menu_item1_name: str = data["localization"][0]["menu_item1_name"]
            menu_item2_name: str = data["localization"][0]["menu_item2_name"]
            search_name: str = data["localization"][0]["search_name"]
            search_placeholder: str = data["localization"][0]["search_placeholder"]
            search_btn_name: str = data["localization"][0]['search_button_name']
            refresh_btn_name: str = data["localization"][0]['refresh_button_name']
            stats_box_name1: str = data["localization"][0]["stats_box_name1"]
            stats_box_name2: str = data["localization"][0]["stats_box_name2"]
            stats_box_items_name: str = data["localization"][0]["stats_box_items_name"]
            db_column1_name: str = data["localization"][0]["db_column1_name"]
            db_column2_name: str = data["localization"][0]["db_column2_name"]
            db_column3_name: str = data["localization"][0]["db_column3_name"]
            insert_button_name: str = data["localization"][0]["insert_button_name"]
            clear_button_name: str = data["localization"][0]["clear_button_name"]
            test_words_filename: str = data["filenames"]["test_words_filename"]
            test_phrases_filename: str = data["filenames"]["test_phrases_filename"]
            insert_vocab_filename: str = data["filenames"]["insert_vocab_filename"]
            clear_vocab_filename: str = data["filenames"]["clear_vocab_filename"]
            print("Success!")
        conn = sqlite3.connect(db)
        c = conn.cursor()
        query = "SELECT word, translation, studied FROM '%s' UNION SELECT word, translation, studied FROM '%s'" % (table1, table2)
        c.execute(query)
        rows = c.fetchall()
        app = MyApp(False)
        app.MainLoop()
    except:
        print("config.json file not found, please add the file to root directory!")
