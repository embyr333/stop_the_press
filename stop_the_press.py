'''
StopThePress - Snapshot2 
Added a GUI*, though have only 'line removal' functionality so far.
(*Adapting my "modstr" code to help remember how to set up a tkinter GUI)

TODO next: add the 'comment out' alternative functionality.
'''

def remove_lines_with_suffix(text: str, suffix: str): 
    if text == '': 
        output_field.insert("end", 'Please enter the code you want to process')
        return # (not essential, just prevents pointless calls)
    lines = text.splitlines()
    for line in lines:
        if not line.endswith(suffix):
            output_field.insert("end", line + '\n')

def submit_click(): # actions for Submit button in GUI below
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

# 'Submit' button on 4th row grid (sets output text in 5th row)
Button(root_widget, text = 'Submit', command = submit_click, bg='#C8C8C8').grid(row=3, column=0)

output_field = ScrolledText(root_widget, width = 120, fg = 'blue', font=("Courier", 10), height=20) # output textbox 
output_field.grid(row=4, column=0) 

root_widget.mainloop()

