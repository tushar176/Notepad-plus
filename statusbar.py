from tkinter import BOTTOM
from tkinter import ttk

'''Here statusbar and functionality of linebar is defined '''

class Statusbar:

    def __init__(self, windows, text_write,linebar):
        self.root = windows
        self.text_write = text_write
        self.linebar=linebar

        self.status_bar = ttk.Label(self.root, text='Status Bar')
        self.status_bar.pack(side=BOTTOM)

        # text_changed -> To work with exit() in  menu.py
        self.text_changed = False

        # '<<Modified>>' -> any change(i,.e; text in text editor)
        self.text_write.text_editor.bind('<<Modified>>', self.changed)

    #-----------------------------------------------Functions----------------------------------------------------------

    #to get the Number of Lines
    def get_line_numbers(self):
        output = ''
        row, col = self.text_write.text_editor.index("end").split('.')  #row give the no of row in text
        #print(int(row)-1)
        for i in range(1, int(row)):
            output += str(i) + '\n'   #making a string with row no. with \n(next line) [for displaying purpose]
        #print(output)
        return output

    #to dispaly the Number of line at the line Bar text field
    def update_line_numbers(self):
        line_numbers = self.get_line_numbers()
        self.linebar.line_number_bar.config(state='normal')
        #changing the font size anf family according to the text editor, if not changed then allignment get disturbed
        self.linebar.line_number_bar.config(font=(self.text_write.current_font_family,self.text_write.current_font_size,'normal'))
        self.linebar.line_number_bar.delete('1.0', 'end')
        self.linebar.line_number_bar.insert('1.0', line_numbers)
        self.linebar.line_number_bar.config(state='disabled')

    #check whether is there and changes in the text field,if any thwn change the values of statusbar & Linebar
    def changed(self, event=None):

        # Change in text editor(i.e; empty to increase in characters)
        if self.text_write.text_editor.edit_modified():
            self.text_changed = True                                        # text editor has some text
            self.text_write.text_editor.get(1.0, 'end-1c').split()  #(start - end-1char) > This delete last char
                                                                    #  because of it count when line changes

            # count word through  split() -> for each word
            words = len(self.text_write.text_editor.get(1.0, 'end-1c').split())
            #count Characters
            characters = len(self.text_write.text_editor.get(1.0, 'end-1c'))
            #count Lines
            row, col = self.text_write.text_editor.index("end").split('.')

            # Shows count of chars & words & Number of Lines
            self.status_bar.config(text=f'Lines: {int(row)-1}  Characters: {characters}  Words: {words}')
            self.status_bar.config(anchor='e')
            self.update_line_numbers()

        # to make code again wheneven there is change in text field
        self.text_write.text_editor.edit_modified(False)
