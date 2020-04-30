import tkinter as tk
from tkinter import colorchooser

class TextWrite:
    '''This class responsible for the textbox and toolbar implementations.
        This include implementations of:
        1. Scrollbar
        2. Font family, font size
        3. Color(for text)
        4. Bold, italic, underline button
        5. Alignments(left, centre, right)'''

    def __init__(self, main_application, toolbar):
        self.root = main_application
        self.toolbar = toolbar

        #Text Editor
        self.text_editor = tk.Text(self.root,font=('Arial',14,'normal'))
        #wrap='word'-->after the end of the line whole world will be taken to the next line
        self.text_editor.config(wrap='word', relief=tk.FLAT)

        self.text_editor.focus_set()       #get cursor focus when windows open


        #Scrollbar
        self.scroll_bar = tk.Scrollbar(self.root)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)                   # Scroll bar on right side of Y axis
        self.text_editor.pack(fill=tk.BOTH, expand=True)                 # show text editor to write
        self.scroll_bar.config(command=self.text_editor.yview)           # This shows scrollbar in y-axis in broadway
        self.text_editor.config(yscrollcommand=self.scroll_bar.set)      # This scroll down the scrollbar when text entered

        #Font
        # Making default font & font size
        self.current_font_family = 'Arial'
        self.current_font_size = 14

        # To Bind Functoinality of changing font, change font size
        self.toolbar.font_box.bind('<<ComboboxSelected>>', self.change_font)
        self.toolbar.font_size.bind('<<ComboboxSelected>>', self.change_font_size)

        # Functionalities of bold, italic, underline, font color, alignments(i.e; centre, right, left)
        self.toolbar.bold_btn.configure(command=self.change_bold)
        self.toolbar.italic_btn.configure(command=self.change_italic)
        self.toolbar.underline_btn.configure(command=self.change_underline)

        self.toolbar.font_color_btn.configure(command=self.change_font_color)         # Font color

        self.toolbar.align_center_btn.configure(command=self.align_center)            # Align Centre
        self.toolbar.align_right_btn.configure(command=self.align_right)              # Align Right
        self.toolbar.align_left_btn.configure(command=self.align_left)                # Align Left

#----------------------------------------Funtions-------------------------------------------------------------#

    def change_font(self, root):
        self.current_font_family = self.toolbar.font_family.get()
        # switching old font type with new font type
        self.text_editor.configure(font=(self.current_font_family, self.current_font_size))

    def change_font_size(self, root):
        self.current_font_size = self.toolbar.size_var.get()
        # switching old font size with new font size
        self.text_editor.configure(font=(self.current_font_family, self.current_font_size))

    def change_bold(self):
        # extract property of font
        text_property = tk.font.Font(font=self.text_editor['font'])

        # font is not bold-> make it bold
        if text_property.actual()['weight'] == 'normal':
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'bold'))

        # font not bold-> make it unbold
        if text_property.actual()['weight'] == 'bold':
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'normal'))

    def change_italic(self):
        # extract property of font
        text_property = tk.font.Font(font=self.text_editor['font'])

        # font is not italic-> make it italic
        if text_property.actual()['slant'] == 'roman':
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'italic'))

        # font is italic-> make it italic
        if text_property.actual()['slant'] == 'italic':
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'roman'))

    def change_underline(self):
        # extract property of font
        text_property = tk.font.Font(font=self.text_editor['font'])

        # font is not underlined-> make it underline
        if text_property.actual()['underline'] == 0:
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'underline'))

        # font is italic-> make it not underlined
        if text_property.actual()['slant'] == 1:
            self.text_editor.configure(font=(self.current_font_family, self.current_font_size, 'normal'))

    def change_font_color(self):
        color_var = tk.colorchooser.askcolor()        # To open color chooser dialogue to select
        self.text_editor.configure(fg=color_var[1])  #  foreground = text color changes with askColor

    def align_center(self):
        self.text_content = self.text_editor.get(1.0, 'end')              # To copy text from start till the end
        self.text_editor.tag_config('center', justify= tk.CENTER)       # justify-> take editor to relavent side(i.e; center)
        self.text_editor.delete(1.0, tk.END)                                # Delete all the text on editor
        self.text_editor.insert(tk.INSERT, self.text_content, 'center'  )# Insert selected content in centre

    def align_right(self):
        self.text_content = self.text_editor.get(1.0, 'end')             # To copy text from start till the end
        self.text_editor.tag_config('right', justify= tk.RIGHT)         # justify-> take editor to relavent side(i.e; right)
        self.text_editor.delete(1.0, tk.END)                           # Delete all the text on editor
        self.text_editor.insert(tk.INSERT, self.text_content, 'right') # Insert selected content in right

    def align_left(self):
        '''Align left'''
        self.text_content = self.text_editor.get(1.0, 'end')             # To copy text from start till the end
        self.text_editor.tag_config('left', justify= tk.LEFT)              # To select character from start till the end
        self.text_editor.delete(1.0, tk.END)                               # Delete all the text on editor
        self.text_editor.insert(tk.INSERT, self.text_content, 'left')     # Insert selected content in left
