import tkinter as tk
from tkinter import ttk,font
'''Toolbar include:
1-font family Combobox
2-font size Combobox
3-BOLD button
4-italic button
5-Underline button
6-font color button
7-Allignment buttons
'''
class Toolbar:
    def __init__(self,main_application):
        self.main_application=main_application

        #basic configuration of main_application
        self.main_application.geometry('1200x800')
        self.main_application.title('Notepad+')
        self.main_application.wm_iconbitmap('icon.ico')

        #making label for toolbar
        self.tool_bar = ttk.Label(self.main_application)
        self.tool_bar.pack(side=tk.TOP, fill=tk.X)

        #Font Combobox
        self.font_tuple = tk.font.families()        # calling All the fonts in a tuple
        self.font_family = tk.StringVar()           # variable to get the Selected font

        #  textvariable=self.font_family --> set the value of font that we get from the User
        # state='readonly' --> the Combobox is not editable, and the user could only select the values from the drop-down list.
        self.font_box = ttk.Combobox(self.tool_bar,
                      width=23,
                      textvariable=self.font_family,
                      state='readonly')

        # Put all  fonts in Font box
        self.font_box['values'] = self.font_tuple

       # Allignment
        self.font_box.grid(row=0, column=0, padx=5)
        self.font_box.current(12)  #setting up default font type = 'Ariel'

        #font size Combobox
        self.size_var = tk.IntVar()
        self.font_size = ttk.Combobox(self.tool_bar,
                     width=5,
                     textvariable = self.size_var,
                      state='readonly')

        # making tuple with values 12 to 59 for the values of font size Combobox
        self.font_size['values'] = tuple(range(12, 60, 1))

        # Allignment
        self.font_size.grid(row=0, column=1, )
        self.font_size.current(2)   # setting up default font size = 14

        ##Bold Button
        self.bold_icon = tk.PhotoImage(file='icons2/bold.png')
        self.bold_btn = ttk.Button(self.tool_bar, image=self.bold_icon)
        self.bold_btn.grid(row=0, column=3, padx=5)

        # Italic Button
        self.italic_icon = tk.PhotoImage(file='icons2/italic.png')
        self.italic_btn = ttk.Button(self.tool_bar, image=self.italic_icon)
        self.italic_btn.grid(row=0, column=4, padx=2)

        # Underline Button
        self.underline_icon = tk.PhotoImage(file='icons2/underline.png')
        self.underline_btn = ttk.Button(self.tool_bar, image=self.underline_icon, )
        self.underline_btn.grid(row=0, column=5, )

        # Font Colour Button
        self.font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
        self.font_color_btn = ttk.Button(self.tool_bar, image=self.font_color_icon,)
        self.font_color_btn.grid(row=0, column=6, padx=2)

        # Align Left
        self.align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
        self.align_left_btn = ttk.Button(self.tool_bar, image=self.align_left_icon, )
        self.align_left_btn.grid(row=0, column=7, padx=2)

        # Align Center
        self.align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
        self.align_center_btn = ttk.Button(self.tool_bar, image=self.align_center_icon, )
        self.align_center_btn.grid(row=0, column=8, padx=2)

        # Align Right
        self.align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
        self.align_right_btn = ttk.Button(self.tool_bar, image=self.align_right_icon, )
        self.align_right_btn.grid(row=0, column=9, padx=2)
