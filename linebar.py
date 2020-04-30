from tkinter import Text

'''here only gui of line bar is implemented its functionality is in statusbar class
dus to some reasons(if here functionality is defined then Allignment and calling made difficult)'''

class Linebar:

    def __init__(self,main_application):
        self.root=main_application

        self.line_number_bar = Text(self.root,width=2, padx=3, takefocus=1,font=('Arial',18,'normal'),
             border=0,background='DarkOliveGreen1', state='disabled',  wrap='none')
        self.line_number_bar.pack(side='left',  fill='y')
