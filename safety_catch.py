#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10795472
#    Student name: Aditya Sant
#
#--------------------------------------------------------------------#

# Import necessary functions
from tkinter import *

# Define some helpful constants
big_font = ('Verdana', 22)

# Create an interactive window
fire_control = Tk()

# Give the window a title
fire_control.title('Safety catch')

def shots_fired():
    if var.get() == 1:
        display.insert(END, 'Bang!      ')
    
var = IntVar()

# Create a text box
display = Text(fire_control, font = big_font, width = 8,
               height = 5, border = 2, relief = 'groove')
display.grid(row = 0, column = 0, padx = 10, pady = 10,
               columnspan = 2)

# Create a push button
fire_button = Button(fire_control, font = big_font, text = ' Fire ', command = shots_fired)
fire_button.grid(row = 1, column = 1, padx = 5, pady = 5)

# Create a check button
enable = Checkbutton(fire_control, font = big_font, text = 'Enable', variable = var, onvalue = 1, offvalue = 0)
enable.grid(row = 1, column = 0, padx = 5, pady = 5)

# Start the interactive event loop
fire_control.mainloop()
