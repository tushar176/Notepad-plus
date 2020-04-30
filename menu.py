import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class Menu():
    def __init__(self,windows,text_write, status_bar, toolbar,linebar):
        self.root = windows
        self.text_write = text_write
        self.statusbar = status_bar
        self.tool_bar_show = toolbar
        self.linebar=linebar

        # Menu configuration
        self.menu = tk.Menu(self.root)
        self.root.configure(menu=self.menu)

#-------------------------------------------------ICONS---------------------------------------------------------------

        #file icons
        self.new_icon = tk.PhotoImage(file='icons2/new.png')
        self.open_icon = tk.PhotoImage(file='icons2/open.png')
        self.save_icon = tk.PhotoImage(file='icons2/save.png')
        self.save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
        self.exit_icon = tk.PhotoImage(file='icons2/exit.png')

        #edit
        self.copy_icon = tk.PhotoImage(file='icons2/copy.png')
        self.paste_icon = tk.PhotoImage(file='icons2/paste.png')
        self.cut_icon = tk.PhotoImage(file='icons2/cut.png')
        self.clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
        self.find_icon = tk.PhotoImage(file='icons2/find.png')

        ###view icons
        self.tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
        self.status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')
        self.line_bar_icon = tk.PhotoImage(file='icons2/line_bar.png')


        #color theme
        self.light_default_icon =  tk.PhotoImage(file='icons2/light_default.png')
        self.light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
        self.dark_icon = tk.PhotoImage(file='icons2/dark.png')
        self.red_icon = tk.PhotoImage(file='icons2/red.png')
        self.monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
        self.night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

#-----------------------------------------------ICONS END-----------------------------------------------------------

#----------------------------------------------CONFIGURING MENU---------------------------------------------------
        # Joining(relate & cascade) sub-menues to main menu
        self.file = tk.Menu(self.menu, tearoff=False)
        self.edit = tk.Menu(self.menu, tearoff=False)
        self.view = tk.Menu(self.menu, tearoff=False)
        self.color_theme = tk.Menu(self.menu, tearoff=False)

        self.menu.add_cascade(menu=self.file, label='File')
        self.menu.add_cascade(menu=self.edit, label='Edit')
        self.menu.add_cascade(menu=self.view, label='View')
        self.menu.add_cascade(menu=self.color_theme, label='Color Theme')


        #  File commands
        ## [].add_command(
        # label -> to show text,
        # image -> put image,
        # comppund -> take string left,
        # accelarator -> To show short cut on right side,
        # command -> to relate function)
        self.file.add_command(label='New', image=self.new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=self.new_file)
        self.file.add_command(label='Open', image=self.open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=self.open_file)
        self.file.add_command(label='Save', image=self.save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command=self.save_file)
        self.file.add_command(label='Save As', image=self.save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=self.save_as)
        self.file.add_command(label='Exit', image=self.exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=self.exit)

        # Edit Menu and functionalities
        # .event_generate("<Control c>") ->  giving commond og copy also binding keyboard for shortcut
        self.edit.add_command(label='Copy', image=self.copy_icon, compound=tk.LEFT, accelerator='Ctrl+C',
                              command=lambda : self.text_write.text_editor.event_generate("<Control c>"))
        self.edit.add_command(label='Paste', image=self.paste_icon, compound=tk.LEFT, accelerator='Ctrl+V',
                               command=lambda : self.text_write.text_editor.event_generate("<Control v>"))
        self.edit.add_command(label='Cut', image=self.cut_icon, compound=tk.LEFT, accelerator='Ctrl+X',
                              command=lambda : self.text_write.text_editor.event_generate("<Control x>"))
        self.edit.add_command(label='Clear All', image=self.clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X',
                              command= lambda : self.text_write.text_editor.delete(1.0, tk.END))
        self.edit.add_command(label='Find', image=self.find_icon, compound=tk.LEFT, accelerator= 'Ctrl+F',
                              command=self.find_replace)

        #View
        self.show_toolbar = tk.BooleanVar()
        self.show_toolbar.set(True)                     # Show toolbar
        self.show_statusbar = tk.BooleanVar()
        self.show_statusbar.set(True)                  # Show statusbar
        self.show_linebar = tk.BooleanVar()
        self.show_linebar.set(True)                  #show line Numbers bar

        ## toolbar Checkbutton
        self.view.add_checkbutton(label='Tool Bar',
            image=self.tool_bar_icon,       # put image
            compound=tk.LEFT,                # put text on left side
            onvalue=True, offvalue=0,        # put values T/F
            variable=self.show_toolbar,      # Responsible for switching T/F
            command=self.hide_toolbar)       # to relate function

        # Statusbar Checkbutton
        self.view.add_checkbutton(label='Status Bar',
            image=self.status_bar_icon,         # put image
            compound=tk.LEFT,                      # put text on left side
            onvalue=True, offvalue=False,      # put values T/F
            variable=self.show_statusbar,       # Responsible for switching T/F
            command=self.hide_statusbar)        # to relate function

          #linebar Checkbutton
        self.view.add_checkbutton(label='Line Numbers',
            image=self.line_bar_icon,         # put image
            compound=tk.LEFT,                      # put text on left side
            onvalue=True, offvalue=False,      # put values T/F
            variable=self.show_linebar,       # Responsible for switching T/F
            command=self.hide_linebar)


        ###Theme Color
        # Put theme
        self.theme_choice = tk.StringVar()

        # theme choices -> images in tuple
        self.color_icons = (self.light_default_icon,
             self.light_plus_icon,
             self.dark_icon,
             self.red_icon,
             self.monokai_icon,
             self.night_blue_icon)

        self.color_dict = {
            'Light Defalut' : ('#000000', '#ffffff'),
            'Light  Plus' : ('#474747', '#e0e0e0'),
            'Dark' : ('#c4c4c4', '#2d2d2d'),
            'Red' : ('#2d2d2d', '#ffe8e8'),
            'Monokai' : ('#d3b774', '#474747'),
            'Night Blue' : ('#ededed', '#6b9dc2')
        }

        # Color Themes Radio button
        for count, item in enumerate(self.color_dict):        # Example:
            self.color_theme.add_radiobutton(label= item,            # 'Light Defalut'
              image= self.color_icons[count],                        # Put image from tuple ->light_default_icon
              variable= self.theme_choice,                            # Set (as StringVar())  only 1 at a time
              compound=tk.LEFT,                                      # Left text
              command=self.change_theme)                             # relate to function


        self.root.bind("<Control-n>", self.new_file)
        self.root.bind("<Control-o>", self.open_file)
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-Alt-s>", self.save_as)
        self.root.bind("<Control-q>", self.exit)
        self.root.bind("<Control-f>", self.find_replace)
        
#---------------------------------------------CONFIGURING MENU END------------------------------------------------------


#---------------------------------------------------Funtions------------------------------------------------------------


#-----------------------------------------functionalities for File----------------------------------------------------
    # New File Function
    def new_file(self):
        #Delete all char
        self.url = ''
        # Delete from start to end
        self.text_write.text_editor.delete(1.0, tk.END)

    #Open File Function
    def open_file(self, event=None):
        #filedialog.askopenfilename -> working path, filetype= ( (Any file name,  txt file extension ), ( All files, Any ext ) )
        self.url = filedialog.askopenfilename(initialdir=os.getcwd(), title= 'Select File', filetype=(('Text File', '*.txt'), ('All files', '*.*')))
        try:
            with open(self.url) as fr: #File read
                self.text_write.text_editor.delete(1.0, tk.END) # if there is already written in text editor it will delete all text
                self.text_write.text_editor.insert(1.0, fr.read()) #insert choosen file in text editor
        except FileNotFoundError:
            return
        except:
            return
        self.root.title(os.path.basename(self.url))

    def save_file(self, event=None):
        try:
            if self.url: # if text file is already open or saved previous version
                content = str(self.text_write.text_editor.get(1.0, tk.END))
                with open(self.url, 'w', encoding='utf-8') as fw: #file writer
                    fw.write(content)
            else:
                    # filedialog.asksaveasfilename(file mode, default extension, file types to write)
                self.url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                content2 = self.text_write.text_editor.get(1.0, tk.END)
                self.url.write(content2)
                self.url.close()
        except Exception as e:
            print(e)
            return


        # save as  Function
    def save_as(self, event=None):
        try:
            content = self.text_write.text_editor.get(1.0, tk.END)
            # filedialog.asksaveasfilename(file mode, default extension, file types to write)
            self.url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            self.url.write(content)
            self.url.close()
        except:
            return
    def exit(self, event=None):
        try:
            if self.statusbar.text_changed: # text_changed = True -> text changed/modified then ask for save the changes or not
                mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file?') # Options -> Yes/No/Cancel
                    # no option forked for -> CANCEL, only for -> YES, NO
                    #if user select -> YES
                if mbox is True:   #we want to change the file
                    if self.url: # file exist in text editor
                        content = self.text_write.text_editor.get(1.0, tk.END) # get from begining to last
                        with open(self.url, 'w', encoding='utf-8') as fw: #filewriter
                            fw.write(content)
                            self.root.destroy() # to cancel window
                    else: #file not exist in text editor
                        content2 = str(self.text_write.text_editor.get(1.0, tk.END))
                            #path to save file-> filedialog.asksaveasfilename(file mode, default extension, file types to write)
                        self.url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                        self.url.write(content2)
                        self.url.close()
                        self.root.destroy()
                    # If User select -> No  , text in  editor and we destroyed it
                elif mbox is False:
                    self.root.destroy()
                # If text_change = False -> editor has no text
            else:
                self.root.destroy()
        except:
            return
#=--------------------------------------------FILE FUNCTIONALITIES END------------------------------------------------

#-------------------------------------------FIND AND REPLACE FUNCTIONS------------------------------------------------
    def find_replace(self,event=None):
        def find():
            word = find_input.get() # getting word from entrybox
            #.tag_remove() ->  removing tag (backforund, foreground)
            #arg( <default word to match>, 1st char of text editor, lastt char of text editor)
            self.text_write.text_editor.tag_remove('match', '1.0', tk.END) # in this module start position is 1;  this means that start from bigining & ends it till the last
            matches = 0
            if word:
                start_pos = '1.0' #single char len
                while True:
                    #to search a word-> arg(searching word, strt pos of text editor, end pos of text editor)
                    start_pos = self.text_write.text_editor.search(word, start_pos, stopindex=tk.END)
                    if not start_pos: # this reads till the & not  found word in text editor
                        break
                    end_pos = f'{start_pos}+{len(word)}c' # c deosnt count spaces
                    self.text_write.text_editor.tag_add('match', start_pos, end_pos)
                    matches += 1
                    start_pos = end_pos
                    #after word found tag changed for spacific word
                    self.text_write.text_editor.tag_config('match', foreground='red', background='yellow')

        def replace():
            #same word from find func
            word = find_input.get()
            replace_text = replace_input.get() # we input in replace entry box
            content = self.text_write.text_editor.get(1.0, tk.END) # 1st - last char from text editor
            new_content = content.replace(word, replace_text)  # word to replace
            self.text_write.text_editor.delete(1.0, tk.END) # delete old word
            self.text_write.text_editor.insert(1.0, new_content) # insert replaceable word

        find_dialogue = tk.Toplevel() # tk.Toplevel() -> window inside window
        find_dialogue.geometry('450x250+500+200') # window size
        find_dialogue.title('Find') # title
        find_dialogue.resizable(0,0) # Not to resize again

        ## frame
        find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
        find_frame.pack(pady=20)

        ## labels
        text_find_label = ttk.Label(find_frame, text='Find : ')
        text_replace_label = ttk.Label(find_frame, text= 'Replace')

        ## entry
        find_input = ttk.Entry(find_frame, width=30)
        replace_input = ttk.Entry(find_frame, width=30)

        ## button
        find_button = ttk.Button(find_frame, text='Find', command=find)
        replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

        ## label grid
        text_find_label.grid(row=0, column=0, padx=4, pady=4)
        text_replace_label.grid(row=1, column=0, padx=4, pady=4)

        ## entry grid
        find_input.grid(row=0, column=1, padx=4, pady=4)
        replace_input.grid(row=1, column=1, padx=4, pady=4)

        ## button grid
        find_button.grid(row=2, column=0, padx=8, pady=4)
        replace_button.grid(row=2, column=1, padx=8, pady=4)

        find_dialogue.mainloop()

#---------------------------------------------FIND AND REPLACE FUNCTIONS END-------------------------------------------

#------------------------------------------------VIEW FUNCTIONS-------------------------------------------------------

    def hide_toolbar(self):
        if self.show_toolbar:  #if toolbar appears
            self.tool_bar_show.tool_bar.pack_forget() # hide toolbar
            self.show_toolbar = False #shows that toolbar is not appearing Checkbutton in now not selected

        #if toolbar not appear  -> Arrange everything again
        else:
             #'''handeling special case when show_linebar,show_statusbar,show_linebar is false and now userwant only to show toolbar'''
            if self.show_statusbar==False and self.show_linebar==False:
                self.text_write.text_editor.pack_forget()
                self.tool_bar_show.tool_bar.pack(side=tk.TOP, fill=tk.X)
                self.text_write.text_editor.pack(fill=tk.BOTH, expand=True)
                self.show_toolbar = True

            else:
                self.text_write.text_editor.pack_forget()  # remove editor
                self.statusbar.status_bar.pack_forget() # remove statusbar
                self.linebar.line_number_bar.pack_forget()  #remove Linebar
                self.tool_bar_show.tool_bar.pack(side=tk.TOP, fill=tk.X)  # again packing toolbar
                self.linebar.line_number_bar.pack(side='left',  fill='y')  #again packing Linebar
                self.text_write.text_editor.pack(fill=tk.BOTH, expand=True) # again packing text editor
                self.statusbar.status_bar.pack(side=tk.BOTTOM)  #aligning statusbar
                self.show_toolbar = True #shows that toolbar is appearing Checkbutton in now selected
    def hide_statusbar(self):
        if self.show_statusbar:  # if statusbar appears already
            self.statusbar.status_bar.pack_forget() # remove status bar
            self.show_statusbar = False #shows that statusbar is not appearing Checkbutton in now not selected
        else :
            self.statusbar.status_bar.pack(side=tk.BOTTOM) # if statusbar doesnt  appear
            self.show_statusbar = True #shows that toolbar is appearing Checkbutton in now selected

    def hide_linebar(self):
        if self.show_linebar:  # if linebar appears already
            self.linebar.line_number_bar.pack_forget()
            self.show_linebar = False  #shows that linebar is not appearing Checkbutton in now not selected
        else:
            self.text_write.text_editor.pack_forget()  # remove editor
            self.statusbar.status_bar.pack_forget() # remove statusbar
            self.linebar.line_number_bar.pack(side='left',  fill='y')
            self.text_write.text_editor.pack(fill=tk.BOTH, expand=True) # aligning text editor
            self.statusbar.status_bar.pack(side=tk.BOTTOM)
            self.show_linebar = True  #shows that linebar is appearing Checkbutton in now selected

#------------------------------------------------VIEW FUNCTIONS END------------------------------------------------

     ## color theme functionality
    def change_theme(self):
        chosen_theme = self.theme_choice.get() # user select what theme directly goes inside
        # choose theme & get value ('#000000', '#ffffff') from  dict  e.g;  'Light Defalut' : ('#000000', '#ffffff')
        color_tuple = self.color_dict.get(chosen_theme)
        fg_color, bg_color = color_tuple[0], color_tuple[1] #color_dict = {  theme : (foreground, background) }
        self.text_write.text_editor.config(background=bg_color, fg=fg_color)


#-------------------------------------------------FUNCTIONS END-------------------------------------------------------
