'''
StopThePress - Snapshot3
Added the 'comment out' alternative functionality.

TODO: Consider whether the code can be refactored to reduce redundancies.
'''

def comment_out_lines_with_suffix(text: str, suffix: str):
    if not text or not suffix: 
        output_field.insert("end", 'Please enter your code and suffix')
        return         
    lines = text.splitlines()
    for i in range(len(lines)):
        if lines[i].endswith(suffix):
            lines[i] = '# ' + lines[i]
        output_field.insert("end", lines[i] + '\n')

def remove_lines_with_suffix(text: str, suffix: str): 
    if not text or not suffix: 
        output_field.insert("end", 'Please enter your code and suffix')
        return 
    lines = text.splitlines()
    for line in lines:
        if not line.endswith(suffix):
            output_field.insert("end", line + '\n')

def comment_out_click(): # actions for Comment Out button in GUI below
    output_field.delete('1.0', END) # clear any existing output
    comment_out_lines_with_suffix(input_field.get("1.0",'end').rstrip(), input_field_2.get("1.0",'end').rstrip()) 

def remove_click(): # actions for Remove button in GUI below
    output_field.delete('1.0', END) # clear any existing output
    remove_lines_with_suffix(input_field.get("1.0",'end').rstrip(), input_field_2.get("1.0",'end').rstrip()) 

# GUI...

from tkinter import *
from tkinter.scrolledtext import ScrolledText
root_widget = Tk()
root_widget.title("stop_the_press removes or comments out (adds # before) lines endng in a specifed suffix")
root_widget.geometry("1010x740") # provisional width, height GUI

Label(root_widget, text = 'Enter code (top box) and suffix (small middle box))').grid(row=0, column=0) 
# (1st row of grid, so row index is 0)

input_field = ScrolledText(root_widget, width = 120, fg = 'blue', font=("Courier", 10), height=20) # input textbox (on 2nd row)
input_field.grid(row=1, column=0, padx=15) 

output = StringVar()

input_field_2 = Text(root_widget, width = 20, fg = 'blue', font=("Courier", 10), height=1)
input_field_2.grid(row=2, column=0, padx=15) 

# Buttons on 4th & 5th rows grid (set output text in 6th row)
comment_out_button = Button(root_widget, text = 'Comment Out', command = comment_out_click, bg='#C8C8C8')
comment_out_button.grid(row=3, column=0)
remove_button = Button(root_widget, text = 'Remove', command = remove_click, bg='#C8C8C8')
remove_button.grid(row=4, column=0)

output_field = ScrolledText(root_widget, width = 120, fg = 'blue', font=("Courier", 10), height=20) # output textbox 
output_field.grid(row=5, column=0) 

root_widget.mainloop()

