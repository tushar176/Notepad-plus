import tkinter as tk
from toolbar import Toolbar
from text_write import TextWrite
from statusbar import Statusbar
from linebar import Linebar
from menu import Menu

main_application = tk.Tk()
toolbar=Toolbar(main_application)
linebar=Linebar(main_application)
text_write = TextWrite(main_application, toolbar)
statusbar = Statusbar(main_application, text_write,linebar)
menu = Menu(main_application,text_write,statusbar, toolbar,linebar)

main_application.mainloop()
