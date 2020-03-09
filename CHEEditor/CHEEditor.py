import os
from tkinter import Menu, Text, Tk, PhotoImage, Toplevel, IntVar, StringVar, BooleanVar, \
    filedialog, messagebox
from tkinter.ttk import Label, Button, Scrollbar, Frame, Entry, Checkbutton, Menubutton

class MainApp():
    def __init__(self):
        self.File_name = None
        self.Programe_Name = "CHE-Editor"
        self.WDG = Tk()
        self.WDG.title(self.Programe_Name)
        self.WDG.iconbitmap("icons/icon_editor.ico")
        self.WDG.geometry("860x620")
        self.WDG.maxsize(width=1340, height=700)
        self.WDG.minsize(width=860, height=620)
        self.Main_UI()

    def Main_UI(self):
        self.MenuBar = Menu(self.WDG)

#1      #MenuBar
        #File_menu
        self.File_menu = Menu(self.MenuBar, tearoff=0, title="File")
        self.MenuBar.add_cascade(label="File", menu=self.File_menu)
        #Edit_menu
        self.Edit_menu = Menu(self.MenuBar, tearoff=0, title="Edit")
        self.MenuBar.add_cascade(label="Edit", menu=self.Edit_menu)
        #View_menu
        self.View_menu = Menu(self.MenuBar, tearoff=0, title="View" )
        self.MenuBar.add_cascade(label="View", menu=self.View_menu)
        #Theme_menu in View
        self.Theme_menu = Menu(self.View_menu, tearoff=0, title="Theme")
        self.View_menu.add_cascade(label="Theme", menu=self.Theme_menu)
        #Option_menu
        self.Options_menu = Menu(self.MenuBar, tearoff=0, title="Options")
        self.MenuBar.add_cascade(label="Options", menu=self.Options_menu)
        #Help_menu
        self.Help_menu = Menu(self.MenuBar, tearoff=0, title="Help")
        self.MenuBar.add_cascade(label="Help", menu=self.Help_menu)

#2      #Icons Variables
        #Edit_Menu Icons
        Undo = PhotoImage(file="icons/Undo.gif")
        Redo = PhotoImage(file="icons/redo.gif")
        Paste = PhotoImage(file="icons/paste.gif")
        Copy = PhotoImage(file="icons/copy.gif")
        Cut = PhotoImage(file="icons/cut.gif")
        #Help_Menu_Icons
        Help = PhotoImage(file="icons/help.gif")
        About = PhotoImage(file="icons/about.gif")
        #File_Menu_Icons
        New = PhotoImage(file="icons/new.gif")
        Open = PhotoImage(file="icons/open.gif")
        Save = PhotoImage(file="icons/save.gif")
        Save_As = PhotoImage(file="icons/save_as.gif")
        Exit = PhotoImage(file="icons/exit.gif")

        #Appear menubar in app
        self.WDG.config(menu=self.MenuBar)
        #self.WDG.config(menu=self.IconBar)

#3      #Set commands in menus
        #File_Menu
        self.File_menu.add_command(label="New", accelerator="Ctrl+N", compound="left",
                                    underline=0, command=self.New)
        self.File_menu.add_command(label="Open", accelerator="Ctrl+O", compound="left",
                                    underline=0, command=self.Open)
        self.File_menu.add_command(label="Save", accelerator="Ctrl+S", compound="left",
                                    underline=0, command=self.Save)
        self.File_menu.add_command(label="Save as", accelerator="Shift+Ctrl+S", compound="left",
                                    underline=0, command=self.Save_As)
        self.File_menu.add_separator()
        self.File_menu.add_command(label="Exit", accelerator="F4", compound="left",
                                    underline=0, command=self.Exit)
        #Edit_Menu
        self.Edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", compound="left",
                                    underline=0, command=self.Undo)
        self.Edit_menu.add_command(label="Redo", accelerator='Ctrl+Y', compound='left',
                                    underline=0, command=self.Redo)
        self.Edit_menu.add_command(label="Select all", accelerator='Ctrl+A', compound='left',
                                    underline=0, command=self.Select)
        self.Edit_menu.add_command(label="Cut", accelerator='Ctrl+X', compound='left',
                                    underline=7, command=self.Cut)
        self.Edit_menu.add_command(label="Copy", accelerator='Ctrl+C', compound='left',
                                    underline=0, command=self.Copy)
        self.Edit_menu.add_command(label="Paste", accelerator='Ctrl+V', compound='left',
                                    underline=0, command=self.Paste)
        self.Edit_menu.add_command(label="Search", accelerator='Ctrl+F', compound='left',
                                    underline=0, command=self.Search)
        #Help_Menu
        self.Help_menu.add_command(label="Help", accelerator="F1", compound="left",
                                    underline=0, command=self.Help)
        self.Help_menu.add_command(label="About", compound="left", underline=0,
                                    command=self.About)
        #View_Menu
        self.Show_line_number = IntVar()
        self.Show_line_number.set(1)
        self.theme_name = StringVar()
        self.View_menu.add_checkbutton(label="Show Line Number", variable=self.Show_line_number)
        self.Highlightline = BooleanVar()
        self.View_menu.add_checkbutton(label='Highlight Current Line',onvalue=1, offvalue=0,
                                variable=self.Highlightline, command=self.Toggle_highlight)
        self.cursorcoord = BooleanVar()
        self.View_menu.add_checkbutton(label='Show Cursor Location', variable=self.cursorcoord,
                                        command=self.Show_cursor_coord)
        self.Theme_menu.add_radiobutton(label="Default", variable=self.theme_name)

#4      #add Shortcut_Bar & Row_Number_Bar
        #Shortcut_Bar
        self.Shortcut_Bar = Frame(self.WDG, height=25)
        self.Shortcut_Bar.pack(expand='no', fill='x')
        Icons = ['New', 'Open', 'Save', 'Copy', 'Cut', 'Paste', 'Undo', 'Redo']
        for i, icon in enumerate(Icons):
            Tool_icon = PhotoImage(file='icons/{}.gif'.format(icon))
            #c_var = 'self.{}'.format(icon)
            cmd = eval('self.{}'.format(icon))
            self.Tool_bar_btn = Button(self.Shortcut_Bar, image=Tool_icon, command=cmd)
            self.Tool_bar_btn.image = Tool_icon
            self.Tool_bar_btn.pack(side='left')
        #Row_Number_Bar
        self.Row_Number_Bar = Text( self.WDG, width=3, padx=3, takefocus=0, border=0,
                                    background='khaki', state='disabled', wrap='none' )
        self.Row_Number_Bar.pack( side='left', fill='y' )

#5      #add Content_Text
        self.Content_Text = Text(self.WDG, wrap='word', undo=1)
        self.Content_Text.pack(expand='yes', fill='both')
        self.Content_Text.tag_configure('active_line', background='ivory2')
        self.Scroll_Bar = Scrollbar(self.Content_Text)
        self.Content_Text.configure(yscrollcommand=self.Scroll_Bar.set)
        self.Scroll_Bar.config(command=self.Content_Text.yview)
        self.Scroll_Bar.pack(side='right', fill='y')

#6      #add_Cursor_Coord_Bar
        self.Cursor_Coord_Bar = Label(self.Content_Text, text='Row: 1 | Column: 1')
        self.Cursor_Coord_Bar.pack(fill=None, expand='no', side='right', anchor='se')

#7      #Binding
        self.Content_Text.bind("<Control-o>", self.Open)
        self.Content_Text.bind("<Control-O>", self.Open)
        self.Content_Text.bind("<Control-s>", self.Save)
        self.Content_Text.bind("<Control-S>", self.Save)
        self.Content_Text.bind("<Shift-Control-KeyPress-s>", self.Save_As)
        self.Content_Text.bind("<Shift-Control-KeyPress-S>", self.Save_As)
        self.Content_Text.bind("<Control-n>", self.New)
        self.Content_Text.bind("<Control-N>", self.New)
        self.Content_Text.bind("<Control-z>", self.Undo)
        self.Content_Text.bind("<Control-Z>", self.Undo)
        self.Content_Text.bind("<Control-y>", self.Redo)
        self.Content_Text.bind("<Control-Y>", self.Redo)
        self.Content_Text.bind("<Control-x>", self.Cut)
        self.Content_Text.bind("<Control-X>", self.Cut )
        self.Content_Text.bind("<Control-a>", self.Select)
        self.Content_Text.bind("<Control-A>", self.Select)
        self.Content_Text.bind("<Control-c>", self.Copy)
        self.Content_Text.bind("<Control-C>", self.Copy)
        self.Content_Text.bind("<Control-v>", self.Paste)
        self.Content_Text.bind("<Control-V>", self.Paste)
        self.Content_Text.bind("<Control-f>", self.Search)
        self.Content_Text.bind("<Control-F>", self.Search)
        self.Content_Text.bind("<Any-KeyPress>", self.Content_changed)
        self.WDG.bind_all("<KeyPress-F1>", self.Help)
        self.WDG.bind_all("<KeyPress-F4>", self.Exit)

#8  #Built In Finctions
    #File_Menu_Functions
    def New(self, event=None):
        self.Content_Text.delete(1., 'end')
        self.WDG.title('{} - {}'.format('Untitled', self.Programe_Name ) )

    ##
    def Open(self, event=None):
        self.Open_file_name = filedialog.askopenfilename(defaultextension=".txt",
                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if self.Open_file_name:
            self.File_name = self.Open_file_name
            self.WDG.title("{} - {}".format( os.path.basename(self.File_name), self.Programe_Name ) )
            self.Content_Text.delete(1.0, 'end')
            with open(self.File_name) as _File:
                self.Content_Text.insert(1.0,  _File.read())

    ##
    def Save(self, event=None):
        if not self.File_name:
            self.Save_As()
        else:
            self.Write_to_file(self.File_name)
        return "break"

    ##
    def Save_As(self, event=None):
        self.Save_file_name = filedialog.asksaveasfilename(defaultextension='.txt',
                                    filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
        if self.Save_file_name:
            self.File_name= self.Save_file_name
            self.Write_to_file(self.File_name)
            self.WDG.title('{} - {}'.format( os.path.basename(self.File_name), self.Programe_Name))
        return "break"

    ##
    def Write_to_file(self, filename):
        try:
            self.content = self.Content_Text.get(1.0, 'end')
            with open(self.File_name, 'w') as the_file:
                the_file.write(self.content)
        except IOError as er:
            print(er)

    ##
    def Exit(self, event=None):
        self.msg_exit = messagebox.askyesno('Exit Editor', 'Do you want to exit?')
        if self.msg_exit:
            self.WDG.destroy()

    #Edit_Menu_Functions
    ##
    def Select(self, event=None):
        self.Content_Text.tag_add("sel", 1.0, "end")
        print("Done1")
        return "breake"

    ##
    def Cut(self, event=None):
        self.Content_Text.event_generate("<<Cut>>")
        return "breake"

    ##
    def Copy(self, event=None):
        self.Content_Text.event_generate("<<Copy>>")
        return "breake"

    ##
    def Paste(self, event=None):
        self.Content_Text.event_generate("<<Paste>>")
        return "breake"

    ##
    def Undo(self, event=None):
        self.Content_Text.event_generate("<<Undo>>")
        return "breake"

    ##
    def Redo(self, event=None):
        self.Content_Text.event_generate("<<Redo>>")
        return "breake"

    ##
    def Search(self, event=None):
        self.Search_Window = Toplevel(self.WDG)
        self.Search_Window.title("Search About...")
        self.Search_Window.transient(self.WDG)
        self.Search_Window.resizable(False, False)
        self.S_lbl_1 = Label(self.Search_Window, text='Search About :')
        self.S_lbl_1.grid(row=0, column=0, sticky='e')
        self.S_ent_1 = Entry(self.Search_Window, width=28)
        self.S_ent_1.grid(row=0, column=1, padx=2, pady=2, sticky='we')
        self.S_ent_1.focus_set()
        Ignore_case_value = IntVar()
        self.S_chk_1 = Checkbutton(self.Search_Window, text='Ignor Case',
                                    variable=Ignore_case_value)
        self.S_chk_1.grid(row=1, column=1, padx=2, pady=2, sticky='e')
        self.S_btn_1 = Button(self.Search_Window, text='Find', underline=0,
                              command=lambda : self.Search_results(
                                    self.S_ent_1.get(), Ignore_case_value.get(),
                                    self.Content_Text, self.Search_Window, self.S_ent_1))
        self.S_btn_1.grid(row=0, column=2, padx=2, pady=2, sticky='e'+'w')
        self.S_btn_2 = Button(self.Search_Window, text='Cancel', underline=0,
                                command=self.Close_Search_Window)
        self.S_btn_2.grid(row=1, column=2, padx=2, pady=2, sticky='e' + 'w')

    ##
    def Search_results(self, Keyword, IfIgnoreCase, Content, Output, Input):
        Content.tag_remove('match', '1.0', 'end' )
        matches_found = 0
        if Keyword:
            start_pos = '1.0'
            while True:
                start_pos = Content.search(Keyword, start_pos, nocase=IfIgnoreCase,
                                                stopindex='end')
                if not start_pos:
                    break
                end_pos = "{} + {}c".format(start_pos, len(Keyword))
                Content.tag_add('match', start_pos, end_pos)
                matches_found += 1
                start_pos = end_pos
            Content.tag_config('match', foreground='red', background='yellow')
            Input.focus_set()
            Output.title("{} matches found".format(matches_found))

    ##
    def Close_Search_Window(self):
        self.Content_Text.tag_remove( 'match', '1.0', 'end' )
        self.Search_Window.destroy()
        #self.Search_Window.protocol('WM_DELETE_WINDOW',self.Close_Search_Window)
        return "break"

    #View_Menu_Functions
    ##
    def Content_changed(self, event=None):
        self.Update_line_numbers()
        self.Update_cursor_coord()

    ##
    def Get_line_numbers(self, event=None):
        self.Number = ""
        if self.Show_line_number.get():
            self.Row, self.Column = self.Content_Text.index('end').split('.')
            for i in range(1, int(self.Row)):
                self.Number += str(i) + "\n"
        return self.Number

    ##
    def Update_line_numbers(self):
        self.Line_Number = self.Get_line_numbers()
        self.Row_Number_Bar.config(state='normal')
        self.Row_Number_Bar.delete(1.0, 'end')
        self.Row_Number_Bar.insert(1.0, self.Line_Number)
        self.Row_Number_Bar.config(state='disabled')

    ##
    def Toggle_highlight(self, event=None):
        if self.Highlightline.get():
            self.Highlight_line()
        else:
            self.Undo_highlight()

    ##
    def Highlight_line(self, interval=100):
        self.Content_Text.tag_remove('active_line', 1.0, 'end')
        self.Content_Text.tag_add('active_line', "insert linestart", "insert lineend+1c")
        self.Content_Text.after(interval, self.Toggle_highlight)

    ##
    def Undo_highlight(self):
        self.Content_Text.tag_remove('active_line', 1.0, 'end')

    ##
    def Show_cursor_coord(self):
        self.cursor_coord_checked = self.cursorcoord.get()
        if self.cursor_coord_checked:
            self.Cursor_Coord_Bar.pack(expand='no', fill=None, side='right', anchor='se')
        else:
            self.Cursor_Coord_Bar.pack_forget()

    ##
    def Update_cursor_coord(self):
        self.Row_2, self.Column_2 = self.Content_Text.index('insert').split('.')
        self.row_num, self.col_num = str(int(self.Row_2)), str(int(self.Column_2) + 1)
        self.Coord = "Row: {} | Column: {}".format(self.row_num, self.col_num)
        self.Cursor_Coord_Bar.config(text=self.Coord)

    #Help_Menu_Functions
    ##
    def About(self, event=None):
        messagebox.showinfo('About', '{} {}'.format(self.Programe_Name, '\nDeveloped by \n TaReK'))

    ##
    def Help(self, event=None):
        messagebox.showinfo('Help', 'Text Editor building in python', icon='question')


if __name__ == "__main__":
    app = MainApp()
    app.WDG.mainloop()