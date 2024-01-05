import wx
import sqlite3
from random import shuffle
import winsound

db = "ItalianStudent.db"
conn = sqlite3.connect(db)
c = conn.cursor()
table_name = "antonimi" 
query = "SELECT word, studied FROM '%s' WHERE studied<100 ORDER BY random()" % table_name
c.execute(query)
rows = c.fetchall()
shuffle(rows)
word = rows[0][0]
studied_number = rows[0][1]
print(word, studied_number)

class Test(wx.App):

    def OnInit(self):
        self.frame = MyFrame(None, title="Italian Test")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MyFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        global count
        count = 0
        print(count)
        

        #Attributes
        #self.SetBackgroundColour("WHITE")
        self.SetIcon(wx.Icon("icon.png"))
        global main_box
        main_box = wx.Panel(self)
        v_sizer = wx.BoxSizer(wx.VERTICAL)
        global main_text
        main_text = wx.StaticText(main_box, label=str(word), style=wx.ALIGN_CENTER_HORIZONTAL|wx.ELLIPSIZE_START)
        font = wx.Font(wx.FontInfo(16).FaceName("Helvetica"))
        main_text.SetFont(font)
        font1 = wx.Font(wx.FontInfo(12).FaceName("Helvetica"))
        global translate_text
        translate_text = wx.StaticText(main_box, style=wx.ALIGN_CENTER_HORIZONTAL|wx.ELLIPSIZE_START)
        translate_text.SetFont(font1)
        global translate_textCtrl
        translate_textCtrl = wx.TextCtrl(main_box)
        translate_textCtrl.SetFont(font)
        #v_sizer.AddSpacer(5)
        v_sizer.Add(main_text,0, wx.EXPAND, 0)
        #v_sizer.AddSpacer(5)
        v_sizer.Add(translate_text,0, wx.EXPAND, 0)
        v_sizer.Add(translate_textCtrl, 0, wx.EXPAND, 0)
        #v_sizer.AddSpacer(10)
        h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddSpacer(10)
        h_sizer1 = wx.GridSizer(3,1,1)
        
        global word_num
        word_num = wx.StaticText(main_box, label="1 of " + str(len(rows)))
        word_num.SetFont(font)

        global score_text
        score_text = wx.StaticText(main_box, label=str(count) + "p.")
        score_text.SetFont(font)
        
        global studied
        studied = wx.StaticText(main_box, label=str(studied_number) + "%")
        studied.SetFont(font)

        global status_text
        status_text = wx.StaticText(main_box,style=wx.ALIGN_CENTER_HORIZONTAL|wx.ELLIPSIZE_START)
        status_text.SetFont(font1)
        
        
        global prev_button
        prev_button = wx.Button(main_box, -1, label="<<")
        prev_button.Disable()
        global check_btn
        check_btn = wx.Button(main_box, -1, label="Check")
        check_btn.Enable()
        translate_btn = wx.Button(main_box, -1, label="Translate")
        global next_button
        next_button = wx.Button(main_box, -1, label=">>")
        prev_button.SetFont(font)
        check_btn.SetFont(font)
        translate_btn.SetFont(font)

        next_button.SetFont(font)

        self.Bind(wx.EVT_BUTTON, lambda evt, a=2: self.OnButton1(evt, a), id=prev_button.GetId())
        self.Bind(wx.EVT_BUTTON, lambda evt, s=studied_number: self.OnButton2(evt, s), id=check_btn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnButton3, id=translate_btn.GetId())
        self.Bind(wx.EVT_BUTTON, lambda evt, a=2: self.OnButton(evt, a), id=next_button.GetId())

        h_sizer.Add(prev_button,1,0,0)
        h_sizer.Add(check_btn,1,0,0)
        h_sizer.Add(translate_btn,1,0,0)
        h_sizer.Add(next_button,1,0,0)
        sizer.Add(status_text, 0, wx.EXPAND, 0)
        #sizer.Add(translate_text)
        h_sizer1.Add(score_text)
        h_sizer1.Add(studied)
        h_sizer1.Add(word_num)
        v_sizer.Add(h_sizer, 0, wx.EXPAND, 0)
        v_sizer.Add(sizer, 0, wx.EXPAND, 0)
        v_sizer.Add(h_sizer1,0, wx.EXPAND | wx.TOP | wx.LEFT, 40, 20)
        main_box.SetSizer(v_sizer)


    def OnButton(self, event, a) -> None:
        
        global main_text
        global translate_textCtrl
        global word_num
        global main_text
        global next_button
        global prev_button
        global check_btn

        if a == len(rows):
            next_button.Disable()

        check_btn.Enable()    
        status_text.SetLabel("")
        translate_text.SetLabel("")
        prev_button.Enable()
        w = rows[a-1]
        s = rows[a-1]
        main_text.SetLabel(w[0])
        studied.SetLabel(str(s[1]) + "%")
        word_num.SetLabel(str(a) + " of " + str(len(rows)))
        self.Bind(wx.EVT_BUTTON, lambda evt, a=a+1: self.OnButton(evt, a), id=next_button.GetId())
        self.Bind(wx.EVT_BUTTON, lambda evt, a=a-1: self.OnButton1(evt, a), id=prev_button.GetId())
        self.Bind(wx.EVT_BUTTON, lambda evt, s=s[1]: self.OnButton2(evt, s), id=check_btn.GetId())
        print(w[0], s[1])

    def OnButton1(self, event, a) -> None:
        global word_num
        global status_text
        global next_button
        global prev_button
        global check_btn

        check_btn.Disable()
        w = rows[a-1]
        s = rows[a-1]
        main_text.SetLabel(w[0])
        studied.SetLabel(str(s[1]) + "%")
        word_num.SetLabel(str(a) + " of " + str(len(rows)))
        self.Bind(wx.EVT_BUTTON, lambda evt, a=a+1: self.OnButton(evt, a), id=next_button.GetId())
        self.Bind(wx.EVT_BUTTON, lambda evt, a=a-1: self.OnButton1(evt, a), id=prev_button.GetId())


    def OnButton2(self, event, s) -> None:
        global score_text
        global count
        global main_text
        global translate_textCtrl
        global status_text
        global check_btn

        def update_studied(studied_add, row):
            convert_studied_add = str(studied_add)
            try:
                conn1 = sqlite3.connect(db)
                c1 = conn1.cursor()
                update_query = "UPDATE '%s' SET studied='%s' WHERE translation='%s' " % (table_name, convert_studied_add, row)
                c1.execute(update_query)
                conn1.commit()
            except sqlite3.Error as error:
                print("Failed to update sqlite table", error)
            finally:
                if conn1:
                    conn1.close()
                    print("The sqlite connection is closed")
            print(update_query)

        correct = main_text.GetLabel()
        value = translate_textCtrl.GetValue()
        correct = str(correct)
        query = "SELECT translation FROM '%s' WHERE word='%s' " % (table_name, correct)
        result = c.execute(query)
        result = c.fetchall()
        row = result[0][0]
        if value == row :
            translate_textCtrl.Clear()
            status_text.SetLabel("True")
            status_text.SetForegroundColour("GREEN")
            studied_add = int(s) + 20
            studied.SetLabel(str(studied_add) + "%")
            update_studied(studied_add, row)
            count +=1
            score_text.SetLabel(str(count) + "p.")
            check_btn.Disable()
            winsound.PlaySound("sounds/true.wav", winsound.SND_FILENAME)
        elif value != row and count > 0:
            translate_textCtrl.Clear()
            check_btn.Disable()
            status_text.SetLabel("False")
            status_text.SetForegroundColour("RED")
            winsound.PlaySound("sounds/false.wav", winsound.SND_FILENAME)
            count -=1
            score_text.SetLabel(str(count) + "p.")
        elif value != row and count == 0:
            translate_textCtrl.Clear()
            check_btn.Disable()
            status_text.SetLabel("False")
            status_text.SetForegroundColour("RED")    
            score_text.SetLabel("0p.")
            winsound.PlaySound("sounds/false.wav", winsound.SND_FILENAME)

        #print(count)

    def OnButton3(self, event) -> None:
        global main_text
        global translate_text
        global check_btn
        correct = main_text.GetLabel()
        query = "SELECT translation FROM '%s' WHERE word='%s'" % (table_name, correct)
        c.execute(query)
        row = c.fetchall()
        translate_text.SetLabel(row[0][0])
        check_btn.Disable()
        winsound.PlaySound("sounds/translate.wav", winsound.SND_FILENAME)
        event.Skip()

if __name__ == "__main__":
    app = Test(False)
    app.MainLoop()
