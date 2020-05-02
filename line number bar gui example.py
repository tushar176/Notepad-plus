import tkinter as tk

def get_line_numbers():
    output = ''
    row, col = text_editor.index("end").split('.')  #row give the no of row in text
    #print(int(row)-1)
    for i in range(1, int(row)):
        output += str(i) + '\n'   #making a string with row no. with \n(next line)
    #print(output)
    return output

def update_line_numbers(event=None):
    line_numbers = get_line_numbers()
    line_number_bar.config(state='normal')
    line_number_bar.delete('1.0', 'end')
    line_number_bar.insert('1.0', line_numbers)
    line_number_bar.config(state='disabled')

def on_content_changed(event=None):
    if text_editor.edit_modified():
        update_line_numbers()
        text_editor.edit_modified(False)


root = tk.Tk()

line_number_bar = tk.Text(root, width=2, padx=3, takefocus=1,font=('Arial',14,'normal'),  border=0,background='DarkOliveGreen1', state='disabled',  wrap='none')
line_number_bar.pack(side='left',  fill='y')


text_editor = tk.Text(root,font=('Arial',14,'normal'))
text_editor.config(wrap='word', relief=tk.FLAT)
text_editor.pack(fill=tk.BOTH, expand=True)


text_editor.bind('<<Modified>>',on_content_changed)
#text_editor.edit_modified(False)
root.mainloop()
